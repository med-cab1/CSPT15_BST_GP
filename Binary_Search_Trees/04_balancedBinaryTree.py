"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean

"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

#Function to find height of a binary tree
def height(root):
    #If tree is empty
    if root is None:
        return 0
    #comparing the heights of the left and right sub-trees
    #to decide the height of the tree
    #maximum value is returned
    return max(height(root.left), height(root.right)) + 1
#function to check tree is balanced or not



def balancedBinaryTree(root):
     #if tree is empty
    if root is None:
        return True
    #finding the height of the left and right sub-tree
    lh = height(root.left)
    rh = height(root.right)
#The values of (lh - rh)  can be 1, -1, 0
    if (abs(lh - rh) <= 1) and balancedBinaryTree(
        root.left) is True and balancedBinaryTree(root.right) is True:
        return True
    
    return False
# def main():
#     #object for Node class
#     root = (15)
#     root.left = (10)
#     root.right = (32)
#     root.left.left = (4)
#     root.left.right = (9)
#     root.left.left.left = (46)
#     root.left.left.right = (52)
#     if balancedBinaryTree(root):
#         print("Tree is balanced")
#     else:
#         print("Tree is not balanced")
# #Driver code
# if __name__ == "__main__":
#     main()
# Output:
#     Tree is not balanced
