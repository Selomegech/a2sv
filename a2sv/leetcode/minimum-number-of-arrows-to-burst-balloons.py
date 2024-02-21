class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 1
        common = [0,0]
        points.sort(key = lambda x:x[0])

        print(points)
        end = points[0][1]
        for i in range(n-1):
            if end < points[i+1][0] :
                ans += 1
                end = points[i+1][1]
                continue
            end = min( end , points[i+1][1])
            # if common == [0,0]:
            #     common[0] = max(points[i][0] , points[i+1][0])
            #     common[1] = min(points[i][1] , points[i+1][1])
            # else:
            #     if common[1] < points[i+1][0]:
            #         ans += 1
            #         common = [0,0]
            #     else:
            #         common[1] =  min(points[i][1] , points[i+1][1])
            
        return ans 




                                           