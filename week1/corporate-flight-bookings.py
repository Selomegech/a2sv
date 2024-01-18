class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n+1)
        for i in range(len(bookings)):
           prefix[bookings[i][0] - 1] += bookings[i][2]
           prefix[bookings[i][1]] -= bookings[i][2]

        
        for i in range (1,len(prefix)):
            prefix[i] += prefix[i-1]
        return prefix [:-1]
 
            
        