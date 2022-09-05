# 429. N-ary Tree Level Order Traversal


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def levelOrder(root):
        # the total number of nodes is between [0, 10 ^ 4]
        # check if root is None to cover 0 node case
        if not root: return []
        # init ans
        ans = []
        # standard bfs approach
        # start with the root node
        q = deque([root])
        # do the following logic when the queue is not empty
        while q:
            # level is used to store all the node values at the current level
            level = []
            # for each element in the current queue
            for _ in range(len(q)):
                # get the first node from the queue and pop it
                node = q.popleft()
                # add it to level
                level += [node.val]
                # this node may include other nodes, we add them all to the queue
                for n in node.children: q.append(n)
            # we've processed this level, add it to ans
            ans += [level]
        # return final ans
        return ans

# Problem Description:
# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

# Example 2:Input:
# root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

# Constraints:

# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]
