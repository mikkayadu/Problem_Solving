class UndergroundSystem:

    def __init__(self):
        self.checkIns = defaultdict(list)
        self.checkOuts = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns[id][-1]
        self.checkOuts[(startStation, stationName)].append(t - startTime)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timeDifference = 0
        divisor = 0

        for time in self.checkOuts[(startStation, endStation)]:
            timeDifference += time
            divisor += 1

        return timeDifference/ divisor 
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)