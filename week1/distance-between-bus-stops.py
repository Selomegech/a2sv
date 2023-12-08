class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total= sum (distance)
        x= min(start, destination )
        y= max(start, destination )

        summ = sum(distance[x:y])
        ans= min(summ, total-summ)
        return ans

        