def transpose(matrix):
    tpose = []
    temp = []
    j = 0
    i = 0
    while True:
        # print(f"matrix[{j}][{i}] = {matrix[j][i]}")
        try:
            temp.append(matrix[j][i])
        except:
            break
        j += 1
        print(j)
        if j == len(matrix):
            tpose.append(temp)
            print(tpose)
            temp = []
            j = 0
            i += 1

    return tpose


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))
