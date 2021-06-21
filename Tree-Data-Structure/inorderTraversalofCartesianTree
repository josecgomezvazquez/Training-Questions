# PROBLEM: Given an inorder traversal of a cartesian tree, construct the tree. Assume duplicates do not exist.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if len(A)==0:
            return None
        maxval = 0
        maxind = 0
        for i in range(len(A)):
            if maxval<A[i]:
                maxval = A[i]
                maxind = i
    
        new_node = TreeNode(maxval)
        new_node.left = self.buildTree(A[:maxind])
        new_node.right = self.buildTree(A[maxind+1:])
        return new_node
