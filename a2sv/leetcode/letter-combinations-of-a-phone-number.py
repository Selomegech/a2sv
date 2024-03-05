class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        path = []
        
        def backtrack(index):
            if index == len(digits):
                result.append(''.join(path))
                return
            
            curr = digits[index]
            letters = dict[curr]
            
            for letter in letters:
                path.append(letter)
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        
        return result