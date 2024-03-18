class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(s):
            for i in s:
                if i.lower() in s and i.upper()  in s:
                    continue
                else:
                    return False
            return True
        ans = ''
        for i in range(len(s)):
            for j in range(i+1 , len(s)):
                if check(s[i : j+1]) and len(ans) < len(s[i : j+1]):
                    ans = s[i : j+1]
        return ans
