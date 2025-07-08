from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None

        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                    node = node.children[c]
                node.word = word
            return root


        # board
        root = build_trie(words)
        row, col = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # prevent duplicates

            board[r][c] = "#"  # mark visited

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            board[r][c] = char  # backtrack

        for r in range(row):
            for c in range(col):
                dfs(r, c, root)

        return result
    
    
# test case
sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(f"Test Case 1: ", sol.findWords(board, words))

board1 = [["a","g", "a", "l"],["m","b","r","o"],["z","u","t","k"],["i","f","l","e"]]
words1 = ["art","broke","eat","zoom"]
print(f"Test Case 1: ", sol.findWords(board1, words1))

