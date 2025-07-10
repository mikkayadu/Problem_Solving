class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(lst):
            return len(set(lst)) == len(lst)

        for i in range(0, 9, 3):
            three_rows = board[i:i+3]
            
            for row in three_rows:
                numbers = []
                for num in row:
                    if num != ".": numbers.append(num)
            
                    if not check(numbers):
                        return False
    

            for j in range(0, 9, 3):
                col1 = []; col2 = []; col3 = []
                for w in range(9):
                    col1.append(board[w][j]) if board[w][j] != "." else None
                    col2.append(board[w][j+1]) if board[w][j+1] != "." else None
                    col3.append(board[w][j+2]) if board[w][j+2] != "." else None

                if not check(col1) or not check(col2) or not check(col3):
                    return False

                three_by_three = []
                for row in three_rows:
                    for val in row[j:j+3]:
                        three_by_three.append(val) if val != "." else None
                
                if not check(three_by_three):
                    return False

        
        return True


            

                    

        