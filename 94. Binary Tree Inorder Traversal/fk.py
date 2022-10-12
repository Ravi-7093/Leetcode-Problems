# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[] #create 2 lists one for result and one to perform stack operations 
        stack=[]
        while True:#while  True
            while(root):
                stack.append(root)#append the values to stack 
                root =root.left#move to the left of the tree
            if not stack:#check if nothing exists on stack
                return res#return res
            node=stack.pop()#pop a value in stack 
            res.append(node.val)#append the node val to list
            root=node.right#move to right of the tree

                
