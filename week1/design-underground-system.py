from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # Stores the check-in information
        self.travel_times = defaultdict(lambda: [0, 0])  # Stores the total travel time and count for each start and end station pair

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_ins[id]
        travelTime = t - startTime
        self.travel_times[(startStation, stationName)][0] += travelTime
        self.travel_times[(startStation, stationName)][1] += 1
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTravelTime, tripCount = self.travel_times[(startStation, endStation)]
        return totalTravelTime / tripCount