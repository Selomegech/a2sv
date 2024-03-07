

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        u = [k for k, _ in intervals]
        y = [h for h, _ in intervals]
        last = [l for _, l in intervals]
        y_sorted = sorted((h, i) for i, h in enumerate(y))
        ans = []
        for x in last:
            r = bisect_right(y_sorted, (x, ))
            if r == len(y_sorted):
                ans.append(-1)
            else:
                i = y_sorted[r][1]
                ans.append(i)
        return ans