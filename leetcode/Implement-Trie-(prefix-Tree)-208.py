class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]    
        t['.'] = '.'
    
    def search(self, word: str) -> bool:
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]    
        return '.' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]    
        return True

# TC : O(n) - len of string
# SC : O(t) - total no.of stored charactors (similar prefix words reuse char)

# Suggested: Trie/Tree
# Key Idea: Implementing a prefix tree using nested dictionaries to efficiently store and retrieve string keys.


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
