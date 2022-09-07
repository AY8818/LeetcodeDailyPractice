# 606. Construct String from Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(root):
        if not root : return ''

        L = self.tree2str(root.left)
        R = self.tree2str(root.right)

        if not L and not R: return f'{root.val}'
        elif L and not R : return f'{root.val}({L})'
        return f'{root.val}({L})({R})'

# Problem Description:
# Given the root of a binary tree, construct a string consisting of parenthesis and integers from
# a binary tree with the preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship
# between the string and the original binary tree.

# Example 1:
# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the
# unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

# Example 2:
# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the first
# parenthesis pair to break the one-to-one mapping relationship between the input and the output.

# Constraints:

# a) The number of nodes in the tree is in the range [1, 104].
# b) -1000 <= Node.val <= 1000
