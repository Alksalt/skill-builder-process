# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        # If the root is None, it's symmetric by definition.
        if not root:
            return True

        # Helper function to check if two subtrees are mirrors of each other.
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # If both subtrees are None, they are mirrors of each other.
            if not t1 and not t2:
                return True
            # If one of the subtrees is None or their values are not equal, they are not mirrors.
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # Recursively check if the left subtree of t1 is a mirror of the right subtree of t2,
            # and if the right subtree of t1 is a mirror of the left subtree of t2.
            return isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        # The tree is symmetric if the left and right subtrees of the root are mirrors of each other.
        return isMirror(root.left, root.right)
