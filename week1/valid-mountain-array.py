class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:  # Check if the array has at least three elements
            return False

        i = 0
        while i < n - 1 and arr[i] < arr[i + 1]:  # Increasing part of the mountain
            i += 1

        if i == 0 or i == n - 1:  # If peak is at the start or end, it's not a valid mountain
            return False

        while i < n - 1 and arr[i] > arr[i + 1]:  # Decreasing part of the mountain
            i += 1

        return i == n - 1  # Return True if we reached the end of the array