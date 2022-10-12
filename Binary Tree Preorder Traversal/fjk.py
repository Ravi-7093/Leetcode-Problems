# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        stack=[]
        while True:
            while(root):
                stack.append(root)#
                res.append(root.val)#append root first
                root=root.left#iterate to left  sub tree
            if not stack:#check if no elements are on stack
                return res
            node=stack.pop()#pop the elements on the stack
            root=node.right#move the node to right
