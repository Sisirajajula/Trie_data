# 
class Solution:
    def replaceWords(self, dictionary, sentence):
        words = sentence.split()
        def searchroot(word, dictionary):
            for i in range(len(word)):
                root = word[0:i]
                if root in dictionary:
                    return root
            return word
        for i in range(len(words)):
            words[i] = searchroot(words[i],dictionary)
        return " ".join(words)
def main():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    replace = Solution()
    result = replace.replaceWords(dictionary, sentence)
    print(result)
if __name__ =="__main__":
    main()


