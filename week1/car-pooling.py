class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1001 
        for num ,fro , to in trips:
            locations[fro] += num
            locations[to] -= num
        people = 0
        for i in locations :
            people += i
            if people > capacity:
                return False
        return True 
