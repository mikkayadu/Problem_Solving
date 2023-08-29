class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        n = len(matrix)
        for row_idx in range(1, len(self.prefix)):
            for col_idx in range( 1, len(self.prefix[0])):
                self.prefix[row_idx][col_idx] = self.prefix[row_idx][col_idx-1] + self.matrix[row_idx-1][col_idx-1]
    
        for col_idx in range(1, len(self.prefix[0])):
            for row_idx in range(1, len(self.prefix)):
                self.prefix[row_idx][col_idx] = self.prefix[row_idx-1][col_idx] + self.prefix[row_idx][col_idx]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - (self.prefix[row2+1][col1-1+1] + self.prefix[row1-1+1][col2+1]) + self.prefix[row1-1+1][col1-1+1]
