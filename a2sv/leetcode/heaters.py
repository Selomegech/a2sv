class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = -1
        right = max(max(houses), max(heaters))
        print(right)
        def helper(mid):
            i = 0
            j = 0
          
            while i < len(houses) and j < len(heaters):

                if (heaters[j] - mid) > houses[i]:
                    return  False
                if (heaters[j] + mid) < houses[i]:
                    j += 1
                else:
                    i += 1
            if i>= len(houses):
                return True
            return False

        while left+1 < right:
            mid = (left + right) // 2

            if helper(mid):
                right = mid
            else:
                left = mid
        return right 

            

                

        