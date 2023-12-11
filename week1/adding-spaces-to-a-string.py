
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_space = 0
        
        for space in spaces:
            result.append(s[prev_space:space])
            prev_space = space
        
        result.append(s[prev_space:])
        
        return ' '.join(result)