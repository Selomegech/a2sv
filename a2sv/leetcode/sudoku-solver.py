class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def findEmptyCell(board):


            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row , col
            return -1 , -1
            


        def isValid(board, row, col, digit):

            for i in range(9):
                if board[row][i] == digit:
                    return False

            for i in range(9):
                if board[i][col] == digit:
                    return False

            startRow = (row // 3) * 3
            startCol = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == digit:
                        return False

            return True


            
            

        def solve(board):
            row , col = findEmptyCell(board)

            if row == -1  and col== -1 :
                return True 
            
            for i in '123456789':
                if isValid(board, row, col, i):
                    board[row][col] = i

                    if solve(board):
                        return True  

                    board[row][col] = '.'
            return False

        solve(board)          