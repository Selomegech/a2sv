class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []

        def generate(left , right):
            if left == right == n:
                ans .append(''.join(path[:]))
                return
            if left < n:
                path.append('(')
                generate(left+1 , right)
                path.pop()
            if left > right :
                path.append(')')
                generate(left , right+1)
                path.pop()
        generate(0 , 0)
        return ans 
            
            
        