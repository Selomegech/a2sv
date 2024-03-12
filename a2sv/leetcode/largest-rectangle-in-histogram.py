class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i , h in enumerate(heights):
            if stack and stack[-1][1] == h:
                continue
            min_start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                min_start = index
                max_area = max(max_area , height * (i - index))
            stack.append((min_start , h))
        return max_area


