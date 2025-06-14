from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            # Check if adding the next word would exceed the line length
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                # Only one word in the line: left-justify
                if len(line) == 1:
                    res.append(line[0] + ' ' * extra_space)
                else:
                    spaces = extra_space // (len(line) - 1)
                    remainder = extra_space % (len(line) - 1)

                    for j in range(remainder):
                        line[j] += ' '  # distribute extra space to the left

                    for j in range(len(line) - 1):
                        line[j] += ' ' * spaces

                    res.append(''.join(line))
                line, length = [], 0

            # Add the current word to the line
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handle the last line: left-justified
        last_line = ' '.join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + ' ' * trail_space)

        return res
