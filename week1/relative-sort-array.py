
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_dict = {num: i for i, num in enumerate(arr2)}
        
        def compare(x):
            if x in order_dict:
                return (0, order_dict[x])
            else:
                return (1, x)
        
        arr1.sort(key=compare)
        return arr1