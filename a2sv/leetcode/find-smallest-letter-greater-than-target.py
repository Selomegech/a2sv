class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        else:
            ans = bisect_right(letters , target)
            return letters[ans] 
        