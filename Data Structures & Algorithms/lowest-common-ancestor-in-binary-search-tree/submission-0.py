# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def LCA(node):
            if p.val < node.val and q.val < node.val:
                return LCA(node.left)
            if p.val > node.val and q.val > node.val:
                return LCA(node.right)
            if (min(p.val, q.val) < node.val and max(p.val, q.val) > node.val) or p.val == node.val or q.val == node.val:
                return node
        return LCA(root)

