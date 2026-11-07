# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in-order traversal, put them into a list, compare each element in the list to see if the previous element is smaller strictly than the current, return True if yes.
        def inorder(node, res):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
        traversal = []
        inorder(root, traversal)
        print(traversal)
        for i in range(1, len(traversal)):
            if traversal[i - 1] >= traversal[i]:
                return False
        return True

