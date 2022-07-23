def deepestLeavesSum(root):
    queue = [root]
    while queue:
        total = 0
        temp_queue = []
        while queue:
            node = queue.pop(0)
            total = total + node.val
            if any([node.left, node.right]):
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
        queue = temp_queue
    return total


root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
print(deepestLeavesSum(root))
