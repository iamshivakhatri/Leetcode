class Solution:
   def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       stack = []
       result = []
       curr = root
       while stack or curr:
           while curr: # This loop adds all the stack whether it is right or left branch of a tree
               stack.append(curr)
               curr = curr.left #even if doesn't point to anything it doesn't matter, it will exit loop and our curr will have the node frm the stack
           curr = stack.pop()
           result.append(curr.val)
           curr = curr.right #even if right doesn't exist, it doesn't matter as in that case it will take the curr from stack again.
       return result
          
