from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        basket = {}
        start = 0

        for end in range(len(fruits)):
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1

            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits