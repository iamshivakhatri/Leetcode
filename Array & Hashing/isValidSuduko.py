class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
#for loop which goes through each elements in the board
        for r in range(len(board)):
            for c in range(len(board[0])):
                #if it doesn't have any character it just passes the loop
                if board[r][c] == '.':
                    continue

                #checking if that element is already in some rows, columns, or in square
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                #adding each element in three different defaultdict that will be rows,columns and squares
                rows[r].add(board[r][c]) 
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
