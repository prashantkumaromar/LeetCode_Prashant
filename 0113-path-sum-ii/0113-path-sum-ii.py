# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.pathSum2(root, targetSum, [], [])
    def pathSum2(self, node, targetSum: int, Current_path, Path_List):
        
        if node is None:
            return 
        Current_path.append(node.val)
        if node.left is None and node.right is None and node.val == targetSum:
            Path_List.append(list(Current_path))
        
        self.pathSum2( node.left, targetSum-node.val, Current_path, Path_List)
        self.pathSum2( node.right,targetSum-node.val, Current_path, Path_List)
        Current_path.pop()
        return Path_List