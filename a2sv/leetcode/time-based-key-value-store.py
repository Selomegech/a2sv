class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value , timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        left = 0
        temp = self.dict.get(key , [])
        right = len(temp)-1
        
        while left <= right:
            mid = (left + right ) // 2
            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return ans 

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)