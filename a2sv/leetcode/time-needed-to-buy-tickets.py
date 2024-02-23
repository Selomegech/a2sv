class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        Q = deque()
        ans = 0
        for i in range(len(tickets)):
         
            Q.append(i)
        
        
        while len(Q) != 0:
            x = Q.popleft()
            if tickets[x] != 0:
                Q.append(x)
                tickets[x] -= 1
                ans += 1
                if x == k and tickets[x] == 0:
                    return ans 
                

        return ans 


            
                
         
            







        