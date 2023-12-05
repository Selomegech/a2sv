class Solution:
    def printVertically(self, s: str) -> List[str]:
        w= list(s.split(" "))
        n= len(max(w,key=len))
        x=[]

        for i in range(n):
            
            curr_word = []
            st=0
            for j in range(len(w)):
                if i >= len(w[j]):
                    st+=1
                else:
                    curr_word.append(" "*st + w[j][i])
                    st = 0

            x.append(''.join(curr_word))
        return x

                
               

        