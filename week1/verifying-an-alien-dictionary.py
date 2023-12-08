class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {c: i for i, c in enumerate(order)}
        
        def compare_words(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if char_order[word1[i]] < char_order[word2[i]]:
                    return -1
                elif char_order[word1[i]] > char_order[word2[i]]:
                    return 1
                i += 1
            
            if len(word1) < len(word2):
                return -1
            elif len(word1) > len(word2):
                return 1
            else:
                return 0
        
        for i in range(1, len(words)):
            if compare_words(words[i-1], words[i]) > 0:
                return False
        
        return True