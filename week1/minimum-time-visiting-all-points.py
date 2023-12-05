from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            
            min_time += max(abs(x2 - x1), abs(y2 - y1))
        
        return min_time

