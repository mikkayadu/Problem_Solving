class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def distinct_check(matrix):
            all_nums = [matrix[i][j] for i in range(3) for j in range(3)]
            
            for i in range(1, 10):
                if i not in all_nums:
                    return False
            return len(all_nums) == len(set(all_nums))

        def check_row(matrix):

            sum1 = sum(matrix[0])
            sum2 = sum(matrix[1])
            sum3 = sum(matrix[2])

            if sum1 != sum2 or sum1 != sum3 or sum2 != sum3:
                return -1

            return sum1
        
        def check_col(matrix):
            print(matrix)
            col1 = sum([matrix[i][0] for i in range(3)])
            col2 = sum([matrix[i][1] for i in range(3)])
            col3 = sum([matrix[i][2] for i in range(3)])

            if col1 != col2  or col1 != col3 or col2 != col3:
                return -1
            return col3
        
        def check_diagonals(matrix):
            prim_diagonal = sum([matrix[i][i] for i in range(3)])
            sec_diagonal = sum([matrix[0][2], matrix[1][1], matrix[2][0]])

            if prim_diagonal != sec_diagonal :
                return -1
            
            return prim_diagonal

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 2 < len(grid) and j + 2 < len(grid[0]):
                    three_by_three = []
                    three_rows = grid[i:i+3]

                    for row in three_rows:
                        three_by_three.append(row[j:j+3])
                    
                    row_sum = check_row(three_by_three)
                    col_sum = check_col(three_by_three)
                    diag_sum = check_diagonals(three_by_three)

                    if row_sum != -1 and col_sum != -1  and diag_sum  != -1:
                        if row_sum == col_sum and row_sum == diag_sum and col_sum == diag_sum and distinct_check(three_by_three):
                            ans += 1
        
        return ans


        