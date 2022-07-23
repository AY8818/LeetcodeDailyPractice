def getRow(rowIndex):
    lst = []
    for i in range(0, rowIndex + 1):
        temp_lst = [1]
        for j in range(0, i):
            if i - 1 == j:
                temp_lst.append(1)
            else:
                temp_lst.append(0)
        lst.append(temp_lst)

    for i in range(2, rowIndex + 1):
        for j in range(1, i):
            try:
                itm = lst[i - 1][j - 1] + lst[i - 1][j]
            except:
                itm = 0
            lst[i][j] = itm

    return lst[rowIndex]


rowIndex = 3
print(getRow(rowIndex))
