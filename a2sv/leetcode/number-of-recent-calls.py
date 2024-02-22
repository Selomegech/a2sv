class RecentCounter:

    def __init__(self):
        self.Q = deque()
        
        

    def ping(self, t: int) -> int:
        # print(self.Q)
        count = 0
        self.Q.append(t)
        q = deque(self.Q)
        
        if t < 3000:
            return len(self.Q)
        r = t-3000
        while len(q) != 0:
            x = q.pop()
            
            if x < r :
                return count
            else:
                count+=1
        return count
        

        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)