class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        x = list(s[:])
        x.reverse()
        
        n = len(s) - 1
        prefix = [0] * len(s)
        for k in range(len(s)):
            if k == 0:
                prefix[k] = 1 if s[k] == '*' else 0
            else:
                prefix[k] = prefix[k-1] + (1 if s[k] == '*' else 0)
        print(prefix)
        def helper(i, j):
            left = i + s[i:j+1] .find('|')
            right = i + s[i:j+1] .rfind('|')
            
            
            print(left , right )
            return (prefix[right] - prefix[left])
            

        for l in queries:
            ans.append(helper(l[0], l[1]))

        return ans