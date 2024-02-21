class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        counter = Counter(answers)
        ans = 0 
        for i,j in counter.items():
            rabbits = i+1
            m = (i +j) // (i+1)
            ans += rabbits * (m)
        return ans 
        