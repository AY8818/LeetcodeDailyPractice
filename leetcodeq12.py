def connect(root):
    lst = []
    level = 1
    level_count = 1
    if len(root) == 1:
        lst.append(root[0])
        lst.append('#')
    elif len(root) == 2:
        lst.append(root[0])
        lst.append('#')
        lst.append(root[1])
        lst.append('#')
    else:
        lst.append(root[0])
        lst.append('#')
        while level <= len(root):
            level = pow(2, level)
            temp = root[level_count:level + 1]
            for i in range(len(temp)):
                if temp[i] != None:
                    lst.append(temp[i])
                try:
                    if temp[i + 1] == None:
                        continue
                except:
                    lst.append('#')
                    break
            level_count = level + 1
            level = level + 1
    return lst


root = [1, 2, 3, 4, 5, None, 7]
print(connect(root))
