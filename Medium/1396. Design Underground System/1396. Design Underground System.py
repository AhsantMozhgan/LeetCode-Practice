# https://leetcode.com/problems/design-underground-system/description/

class UndergroundSystem:

    def __init__(self):
        self.check_in_data = dict()
        self.travel_times = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        travel_time = t - start_time

        route = (start_station, stationName)

        if route not in self.travel_times:
            self.travel_times[route] = [0, 0]

        self.travel_times[route][0] += travel_time
        self.travel_times[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)