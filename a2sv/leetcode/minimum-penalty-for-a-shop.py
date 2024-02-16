class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_sum = [0] * (n + 1)
        min_penalty = float('inf')
        min_hour = -1

        
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + (customers[i-1] == 'N')

        
        for hour in range(n+1):
            penalty = prefix_sum[hour] + (n - hour - (prefix_sum[n] - prefix_sum[hour]))

            
            if penalty < min_penalty:
                min_penalty = penalty
                min_hour = hour

        return min_hour