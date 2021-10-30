# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack= list()
        flag = True
        def inorder(root):
            if root.left:
                inorder(root.left)
            stack.append(root.val)
            if root.right:
                inorder(root.right)
        def isSorted(stack, flag):
            for x in range(1,len(stack)):
                if stack[x-1] >= stack[x]:
                    flag = False
                    print(flag)
            return flag
        inorder(root)
        ans = isSorted(stack,flag)
        return ans