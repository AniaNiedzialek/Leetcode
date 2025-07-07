class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True      

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# test cases


# ...existing code...

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))    # Expected: False
    print(wd.search("bad"))    # Expected: True
    print(wd.search(".ad"))    # Expected: True
    print(wd.search("b.."))    # Expected: True
    print(wd.search("b.d"))    # Expected: True
    print(wd.search("..d"))    # Expected: True
    print(wd.search("..."))    # Expected: True
    print(wd.search("...."))   # Expected: False
    wd.addWord("b")
    print(wd.search("b"))      # Expected: True
    print(wd.search("."))      # Expected: True

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))    # Expected: False
    print(wd.search("bad"))    # Expected: True
    print(wd.search(".ad"))    # Expected: True
    print(wd.search("b.."))    # Expected: True
    print(wd.search("b.d"))    # Expected: True
    print(wd.search("..d"))    # Expected: True
    print(wd.search("..."))    # Expected: True
    print(wd.search("...."))   # Expected: False
    wd.addWord("b")
    print(wd.search("b"))      # Expected: True
    print(wd.search("."))      # Expected: True