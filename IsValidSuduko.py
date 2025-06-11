class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
       rows = collections.defaultdict(set)
       cols = collections.defaultdict(set)
       square = collections.defaultdict(set)


       for i in range(len(board)):
           for j in range(len(board[0])):
               val = board[i][j]
               if val == ".":
                   continue
               if val in rows[i] or val in cols[j] or val in square[(i//3, j//3)]:
                   return False
               rows[i].add(val)
               cols[j].add(val)
               square[(i//3, j//3)].add(val)


       return True


      

