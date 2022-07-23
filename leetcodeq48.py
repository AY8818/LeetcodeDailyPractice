# def generate(numRows):
#     lst = []
#     for i in range(1, numRows + 1):
#         temp = []
#         for j in range(0, i):
#             temp.append(0)
#         lst.append(temp)
#     lst[0][0] = 1
#     for i in range(1, numRows):
#         lst[i][0] = 1
#         j = len(lst[i]) - 1
#         lst[i][j] = 1

#     for i in range(2, numRows):
#         for j in range(1, len(lst[i - 1])):
#             try:
#                 itm = lst[i - 1][j]
#             except:
#                 itm = 0
#             lst[i][j] = lst[i - 1][j - 1] + itm
#     print(lst)
#

# Faster than above method
def generateFaster(numRows):
    lst = [[1], [1, 1]]
    if numRows <= 2:
        return lst[:numRows]
    count = 2
    while count < numRows:
        prev_sublst = lst[count - 1]
        curr_sublst = []
        for i in range(count + 1):
            if i == 0:
                curr_sublst.append(prev_sublst[0])
            elif i == count:
                curr_sublst.append(prev_sublst[count - 1])
            else:
                curr_sublst.append(prev_sublst[i] + prev_sublst[i - 1])
        lst.append(curr_sublst)
        count += 1
    return lst


numRows = 2
print(generateFaster(numRows))
