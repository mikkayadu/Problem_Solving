class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0])-1
        u, d = 0, len(matrix) -1

        while l < r and u < d:
            top_row = []
            for i in range(l, r+1):
                top_row.append(matrix[u][i])
            
            left_col = []
            for c in range(u+1, d+1):
                left_col.append(matrix[c][l])
            
            right_col = []
            for i in range(u+1, d+1):
                right_col.append(matrix[i][r])

            bottom_row = []
            for i in range(l, r+1):
                bottom_row.append(matrix[d][i])

            print(top_row, left_col, right_col, bottom_row)

            j = 0
            for i in range(u, d+1):
                matrix[i][r] = top_row[j]
                j+= 1
            
            j = 0
            left_col.reverse()
            for i in range(l, r):
                matrix[u][i] = left_col[j]
                j+=1
            
            j = 0
            right_col.reverse()
            for i in range(l, r):
                matrix[d][i] = right_col[j]
                j+=1
            
            j = 0
            for i in range(u, d):
                matrix[i][l] = bottom_row[j]
                j += 1

            print(matrix)
            l+=1; r-=1; u+=1; d-=1




        