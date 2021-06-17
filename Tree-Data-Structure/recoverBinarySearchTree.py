# PROBLEM: Two elements of a binary search tree (BST) are swapped by mistake.
#          Return the 2 values swapping which the tree will be restored.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        #Solution using moris traversal
        current = A
        result = []
        prev = -1000000000000
        while current is not None: 
            #If there is no left subtree, visit the node and then node to its right
            if current.left is None: 
                #If anomaly is found, then add to result
                if prev > current.val:
                    result.append(prev)
                    result.append(current.val)
                #setting prev 
                prev = current.val
                # Visiting node to right
                current = current.right 
            #If left subtree is present
            else: 
                #For creating link between predecessor and successor, storing predecesor in variable
                pre = current.left
                #Going for successor
                while pre.right is not None and pre.right is not current: 
                    pre = pre.right 
                if pre.right is None: 
                    pre.right = current 
                    current = current.left     
                #After traversing is done, reseting changes done by Morris traversal
                else: 
                    #Again checking for anomaly
                    if current.val < prev:
                        result.append(prev)
                        result.append(current.val)
                    pre.right = None
                    prev = current.val 
                    current = current.right
        result.sort()
        #len(result) is 4 when elements swapped are not adjacent and first and fourth element are final answer 
        if len(result) == 4:
            del result[1]
            del result[1]
        return result
