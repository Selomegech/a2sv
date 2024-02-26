class Solution:
    def pow(self , x , y ,  mod):
            if y == 1 :
                return x
            if y < 1:
                return 1
            val = self.pow(x , y//2,mod)
            if y % 2 == 0:
                return(val * val ) % mod
            if y % 2 == 1:
                return(val * val * x) % mod 
    def countGoodNumbers(self, n: int) -> int:
        
            

            
        mod=10**9 + 7
        tot=1
        if n %2 ==0 :
            tot*=self.pow(5,n//2,mod)
            tot*=self.pow(4,n//2,mod)
            tot%=mod
            
        else:
            tot*=self.pow(5,(n//2)+1,mod)
            tot*=self.pow(4,n//2,mod)
            tot%=mod
        return tot