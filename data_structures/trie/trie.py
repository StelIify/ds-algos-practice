class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def insert(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                # If the current character isn't found among
                # the current node's children, we add
                # the character as a new child node:
                new_node = TrieNode()
                current_node.children[char] = new_node

                current_node = new_node
        current_node.children["*"] = None

    def collect_all_words(self, node=None, word='', words=None):
        if words is None:
            words = []
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(child_node, word + key, words)
        return words

    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collect_all_words(current_node)

    def autocorrect(self, word):
        current_node = self.root
        word_so_far = ""

        for char in word:
            if current_node.children.get(char):
                word_so_far += char
                current_node = current_node.children[char]
            else:
                return word_so_far + self.collect_all_words(current_node)[0]
        return word


words_to_test = ["cat", "car", "cherry", "cool", "cup", "carrot", "control"]
trie = Trie()
for word in words_to_test:
    trie.insert(word)

print(trie.autocomplete("c"))
# print(trie.collect_all_words())
print(f'Did you mean {trie.autocorrect("cherru")}')



