from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        path = []
        x = 1
        
        def combine(x):
            if len(path) == k:
                if sum(path) == n:
                    ans.add(tuple(path))
                return
            for i in range(x, 10):
                path.append(i)
                combine(i + 1)
                path.pop()
        
        combine(x)
        return list(ans) 