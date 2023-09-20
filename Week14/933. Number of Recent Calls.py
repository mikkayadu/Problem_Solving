class RecentCounter:

    def __init__(self):
        self.q = []
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        valid = t - 3000
        while valid > 0 and self.q[0] < valid:
            self.q.pop(0)
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
