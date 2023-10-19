class Solution:
    def check_repetition(self, mylist:list):
        modified = [i for i in mylist if i!='.']
        if len(modified) != len(set(modified)):
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows for repetion

        for row in board:
            if self.check_repetition(row):
                return False
        
        
        
        for col in range(9):
            columns = []
            for row in range(9):
                columns.append(board[row][col])
            
            if self.check_repetition(columns):
                return False
        

        for i in range(0, 9, 3):
            three_rows = board[i:i+3]
            
            # print("three_rows", three_rows)
            
            for j in range(0, 9, 3):
                temp = []; p_temp = []
                for row in three_rows:
                    temp.append(row[j:j+3])
                print(temp)
                for lst in temp:
                    for value in lst:
                        p_temp.append(value)
                
                if self.check_repetition(p_temp):
                    return False
        return True
