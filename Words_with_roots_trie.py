class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.childNode = [None] * 26
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not cur.childNode[index]:
                cur.childNode[index] = TrieNode()
            cur = cur.childNode[index]
        cur.wordEnd = True
    def shortroot(self, word):
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not cur.childNode[index]:
                return word
            cur = cur.childNode[index]
            if cur.wordEnd:
                return word[:i + 1]
        return word
class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        words = sentence.split()
        dict = Trie()
        for word in dictionary:
            dict.insert(word)
        for i in range(len(words)):
            words[i] = dict.shortroot(words[i])
        return " ".join(words)
def main():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    replace = Solution()
    result = replace.replaceWords(dictionary, sentence)
    print(result)
if __name__ =="__main__":
    main()