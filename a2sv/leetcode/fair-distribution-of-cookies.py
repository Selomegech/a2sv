class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        children = [0] * k
        
        def backtrack(i):
            nonlocal ans
            if i == len(cookies):
                u = max(children)
                ans = min(ans , u)
                return

            for j in range(k):
                
                children[j] += cookies[i]
                if children[j] < ans:
                    backtrack(i+1)
                children[j] -= cookies[i]
        backtrack(0)
        return ans

         