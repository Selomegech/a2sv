class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        matrix=[]
        walls_= set()
        for i in walls:
            walls_.add(tuple(i))
        for i in guards:
            walls_.add(tuple(i))
            

        for i in range(m):
            matrix.append([0]*n)

        for i in range (len(guards)):
            x=guards[i][0]
            y=guards[i][1]
            while x+1 < m:
                x+=1
                if (x,y) in walls_ :
                    break
                else:
                    matrix[x][y]=1
                
            x=guards[i][0]
            while x-1>=0:
                x-=1
                if (x,y) in walls_:
                    break
                else:
                    matrix[x][y]=1

                    
                
            x=guards[i][0]
            while y+1 < n:
                y+=1
                if (x,y) in walls_:
                    break
                else:
                    matrix[x][y]=1
                
            
            y=guards[i][1]
            while y-1>=0:
                y-=1
                if (x,y) in walls_:
                    break
                else:
                    matrix[x][y]=1
                
        result = 0 
        print(matrix)
        for i in range(m):
            for j in range (n):
                if matrix[i][j] != 1:
                    result += 1
        result -= len(walls_)
        return result

        
            

        # total = n * m
        # print(guarded , len(guarded),total)
        # result= total - guarded_
        # return (result)
    
            
        