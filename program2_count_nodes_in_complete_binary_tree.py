"""
Experiment 9: Graphs and Dynamic Programming
Program 2: Count Nodes in Complete Binary Tree
Aim: Count nodes in a complete binary tree using traversal.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(count_nodes(root))
