class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stack = []
        for el in nums2:
            while stack and stack[-1] < el:
                dict[stack[-1]] = el
                stack.pop()
            stack.append(el)
        while stack:
            dict[stack[-1]] = -1
            stack.pop()
        ans = []
        for el in nums1:
            ans.append(dict[el])
        return ans


         