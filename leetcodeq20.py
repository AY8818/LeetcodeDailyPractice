# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
def getTargetCopy(original, cloned, target):
    if original is None:
        return
    elif original == target:
        return cloned
    # else:
    #     return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)


original = [7]
cloned = original
target = 7
print(getTargetCopy(original, cloned, target))
