# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        else:
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)
            
            root.left = self.buildTree(inorder[0:root_index], postorder[: root_index] )
            root.right = self.buildTree(inorder[root_index+1 :], postorder[root_index:])
           
        return root
        
        