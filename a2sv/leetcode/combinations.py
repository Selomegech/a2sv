class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        path = []

        def backtrack(first , n , k):
            if len(path) == k:
                ans.append(path[:])

            for i in range(first , n+1):
                path.append(i)
                backtrack(i+1 , n , k)
                path.pop()
        backtrack(1 , n ,k)
        return (ans)


            


        