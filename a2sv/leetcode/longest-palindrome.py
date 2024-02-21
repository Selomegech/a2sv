class Solution:
    def longestPalindrome(self, s: str) -> int:
        foundOne = False
        n = len(s)
        counter = Counter(s)
        # # print(counter , len(counter), counter[0] , counter[1])
        # if len(counter) == 1:
        #     return n
        
        first = False 
        for i,j in counter.items():
            
            
            if j %2 != 0 and foundOne == False:
                foundOne = True
                continue
            if j %2 !=0 and foundOne:
                n -= 1
                continue
            if j % 2 != 0:
                n -= 1
                # print(i , j)
        return n








        