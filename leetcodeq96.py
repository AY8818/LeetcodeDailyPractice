# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def goodNodes(root):
    def solve(node, max_so_far):
        if not node:
            return 0
        res = 0
        if node.val >= max_so_far:
            res += 1
            max_so_far = node.val
        res += solve(node.left, max_so_far)
        res += solve(node.right, max_so_far)
        return res
    return solve(root, root.val)


root = [3,1,4,3,null,1,5]

# Problem Description:
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there
# are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Example 2:
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

# Constraints:
# a) The number of nodes in the binary tree is in the range [1, 10^5].
# b) Each node's value is between [-10^4, 10^4].
