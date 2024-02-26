class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 + 7
        tot=1
        if n %2 ==0 :
            tot*=pow(5,n//2,mod)
            tot*=pow(4,n//2,mod)
            tot%=mod
            
        else:
            tot*=pow(5,(n//2)+1,mod)
            tot*=pow(4,n//2,mod)
            tot%=mod
        return tot