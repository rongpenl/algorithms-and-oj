# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        if (root.left == None and root.right == None):
            return True
        return self.isReverseTree(root.left, root.right)

    def isReverseTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        else:
            return self.isReverseTree(p.left, q.right) and self.isReverseTree(p.right, q.left)
