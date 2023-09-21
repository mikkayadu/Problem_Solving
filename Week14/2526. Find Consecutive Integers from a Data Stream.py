class DataStream:

    def __init__(self, value: int, k: int):
        self.q = []
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0

        if self.count >= self.k:
            return True
        else:
            return False
        
