class Solution:
    

    def sumSubarrayMins(self ,arr: List[int]) -> int:
        length = len(arr)
        left = [-1] * length
        right = [length] * length
        
        stack = deque()
        
        for i in range(length):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack.clear()
        
        for i in range(length - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        mod = int(1e9) + 7
        answer = 0
        
        for i in range(length):
            answer += ((i - left[i]) * (right[i] - i) % mod * arr[i]) % mod
            answer %= mod
        
        return int(answer)