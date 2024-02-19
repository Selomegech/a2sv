class Solution:
    def numberOfWays(self, s: str) -> int:
        l = len(s)
        p0 = [0] * l
        p1 = [0] * l
        p01 = [0] * l
        p10 = [0] * l
        p010 = [0] * l
        p101 = [0] * l

        for i in range(l):
            p0[i] = p0[i-1] + (s[i] == '0')
            p1[i] = p1[i-1] + (s[i] == '1')

        for i in range(l):
            if s[i] == '0':
                p01[i] = p01[i-1]
                p10[i] = p10[i-1] + p1[i]
            else:
                p01[i] = p01[i-1] + p0[i]
                p10[i] = p10[i-1]

        for i in range(l):
            if s[i] == '0':
                p010[i] = p010[i-1] + p01[i]
                p101[i] = p101[i-1]
            else:
                p010[i] = p010[i-1]
                p101[i] = p101[i-1] + p10[i]

        ans = p101[-1] + p010[-1]
        # print(p1 )
        # print(p0)
        # print(p10 )
        # print(p01)
        # print(p101 )
        # print(p010)
        return ans 





        