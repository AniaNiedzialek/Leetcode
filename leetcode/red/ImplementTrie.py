
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# ...existing code...

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # Expected: True
    print(trie.search("app"))      # Expected: False
    print(trie.startsWith("app"))  # Expected: True
    trie.insert("app")
    print(trie.search("app"))      # Expected: True
    print(trie.startsWith("appl")) # Expected: True
    print(trie.startsWith("banana")) # Expected: False
    trie.insert("banana")
    print(trie.search("banana"))   # Expected: True
    print(trie.search("ban"))      # Expected: False
    print(trie.startsWith("ban"))  # Expected: True