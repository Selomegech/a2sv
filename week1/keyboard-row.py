class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the three rows of the keyboard
        rows = [
            set("QWERTYUIOP"),
            set("ASDFGHJKL"),
            set("ZXCVBNM")
        ]
        
        result = []
        
        for word in words:
            # Convert the word to uppercase for case-insensitive comparison
            upper_word = word.upper()
            
            # Check if all characters in the word are from a single row
            if any(set(upper_word) <= row for row in rows):
                result.append(word)
        
        return result   