def isValid(s):
    begin = ['(', '[', '{']
    end = [')', ']', '}']
    queue = []
    if s[0] in end:
        return False
    if s[len(s) - 1] in begin:
        return False
    for i in s:
        if i in begin:
            queue.append(i)
        elif i in end and len(queue) != 0:
            indx = end.index(i)
            if queue[len(queue) - 1] == begin[indx]:
                queue.pop(len(queue) - 1)
            else:
                return False
        elif i in end and len(queue) == 0:
            return False

    if len(queue) == 0:
        return True
    else:
        return False


s = "[])"

print(isValid(s))
