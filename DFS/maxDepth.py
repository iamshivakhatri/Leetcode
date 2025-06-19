# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def maxDepth(self, root: Optional[TreeNode]) -> int:
       stack = [[root, 1]]
       res = 0
       while stack: #created datastructure
           node, depth = stack.pop() 
           if node:#root node of tree so check if it is empty
               res = max(depth, res) #gets the maximum
               stack.append([node.left, depth + 1])
               stack.append([node.right, depth+1])
       return res

