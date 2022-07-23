def isValidSudoku(board):

    # print(board[0][0])
    for i in range(9):
        for j in range(9):
            #print("i = ", i)
            #print("j = ", j)

            if board[i][j] != ".":
                item = board[i][j]
            else:
                continue
            # Finding duplicates in row i
            if board[i].count(item) > 1:
                return("Duplicate Found in row")
            else:  # Finding duplicates in column j
                x = i
                lst = []
                for x in range(9):
                    if board[x][j] != ".":
                        lst.append(board[x][j])
                if lst.count(item) > 1:
                    return("Duplicate found in column")

    itr = 0
    j = 0

    for i in range(9):

        itr = 0
        lst = []
        while itr <= 8:
            if j < 3:
                if board[i][j] != ".":
                    lst.append(board[i][j])
            if j == 2 and i in [0, 1, 2]:
                j = 0
                i = i + 1
            if j < 6:
                if board[i][j] != ".":
                    lst.append(board[i][j])
            if j == 5 and i in [3, 4, 5]:
                j = 0
                i = i + 1
            if j < 9:
                if board[i][j] != ".":
                    lst.append(board[i][j])
            if j == 8 and i in [6, 7, 8]:
                j = 0
                i = i + 1
            j = j + 1
            itr = itr + 1

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(isValidSudoku(board))
