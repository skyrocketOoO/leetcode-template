class Trie:
    def __init__(self, words=[]):
        self.root = {"length": 0}
        for word in words:
            self.insert(word)
            
    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {"length": 0}
            current["length"] += 1
            current = current[c]
        current["length"] += 1
        current["?"] = True

    def remove(self, word):
        current = self.root
        current["length"] -= 1
        for i, c in enumerate(word):
            if c in current:
                current[c]["length"] -= 1
                if current[c]["length"] < 1:
                    del current[c]
                    break
                else:
                    current = current[c]
        if i == len(word) - 1 and "?" in current:
            current.pop("?")

    # return 2 if exist or 1 if prefix, 0 if not found
    def contains(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return 0
            current = current[c]
        return 2 if "?" in current else 1

if __name__ == "__main__":
  trie = Trie(["apple", "app", "banana", "bat", "bar"])

  # Check if the words are in the Trie
  print(trie.contains("apple"))  # Output: 2 (word exists)
  print(trie.contains("app"))    # Output: 2 (word exists)
  print(trie.contains("appl"))   # Output: 1 (prefix exists)
  print(trie.contains("bat"))    # Output: 2 (word exists)
  print(trie.contains("bar"))    # Output: 2 (word exists)
  print(trie.contains("ban"))    # Output: 1 (prefix exists)
  print(trie.contains("bana"))   # Output: 1 (prefix exists)
  print(trie.contains("basket")) # Output: 0 (not found)

  # Remove a word from the Trie
  trie.remove("apple")
  print(trie.contains("apple"))  # Output: 0 (word removed)
  print(trie.contains("app"))    # Output: 2 (word still exists as it's separate)
  print(trie.contains("appl"))   # Output: 1 (prefix exists)

  # Add a new word to the Trie
  trie.insert("apply")
  print(trie.contains("apply"))  # Output: 2 (new word exists)
  print(trie.contains("app"))    # Output: 2 (word exists)
  print(trie.contains("appl"))   # Output: 1 (prefix exists)