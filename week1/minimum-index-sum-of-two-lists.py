class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = {}
        min_sum = float('inf')
        result = []

        for i, restaurant in enumerate(list1):
            index_sum[restaurant] = i

        for i, restaurant in enumerate(list2):
            if restaurant in index_sum:
                curr_sum = i + index_sum[restaurant]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [restaurant]
                elif curr_sum == min_sum:
                    result.append(restaurant)

        return result