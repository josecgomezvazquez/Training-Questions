# PROBLEM: Given a binary tree, return the inorder traversal of its nodes' values without using recursion.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        self.stack = []
        self.result = []
        node = A
        while(self.stack or node):
            if node:
                self.stack.append(node)
                node = node.left
            else:
                node = self.stack.pop()
                self.result.append(node.val)
                node = node.right
        #print(self.result)
        return self.result
