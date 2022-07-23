def totalNQueens(n):
    board = []
    for _ in range(n):
        t = ["."]*n
        board.append(t)
    print(board)
    pos = []

    def addQueenToPos(prevPos):
        print("\nFunction begin ##########")
        nextPos = -1
        # print("\nnextPos = ",nextPos)

        print(f"if prevPos != -1: {prevPos != -1}")
        if prevPos != -1:

            print("While Loop begin --")
            while True:
                print("\n-----------------")

                nextPos = nextPos + 1;
                print("Modify nextPos = ",nextPos)

                print(f"if nextPos not in pos: {nextPos not in pos}")
                if nextPos not in pos and nextPos<n and nextPos not in alreadyVisted:

                    print(f"if nextPos != prevPos-1 and nextPos!=prevPos+1:{nextPos != prevPos-1 and nextPos!=prevPos+1}")
                    if nextPos != prevPos-1 and nextPos!=prevPos+1:
                        print("True")
                        return nextPos

                    elif nextPos == prevPos-1 or nextPos == prevPos + 1:
                        print(f"elif nextPos == prevPos-1 or nextPos == prevPos + 1:")
                        print("True")
                        print("continue")
                        continue

                elif nextPos>=n:
                    print("elif nextPos>=n:")
                    print("True")
                    print("return backtrack\n")
                    return "backtrack"

                elif nextPos in pos:
                    continue

        elif prevPos == -1:
            print("return 0")
            return 0


    prevPos = -1

    alreadyVisted = []

    Queen = 0

    while Queen<n:
        print(f"\nFor Queen = {Queen}")
        print(f"calling function addQueenToPos({prevPos})")

        nxtPos = addQueenToPos(prevPos)
        print("Function end xxxxxxxxxxx\n")

        print(f"nxtPos = {nxtPos}")

        print(f"if nxtPos != 'backtrack': {nxtPos != 'backtrack'}")
        if nxtPos != "backtrack":

            print(f"if nxtPos not in pos: {nxtPos not in pos}")
            if nxtPos not in pos:
                pos.append(nxtPos)
                print(f"add {nxtPos} to pos")
                print("pos = ",pos)
                prevPos = nxtPos
                print("Set prevPos = ",prevPos)

            Queen += 1
            print("CONTINUE")
            continue

        else:
            try:
                t = pos.pop()
                alreadyVisted.append(t)
            except:
                pass

            print("Remove last Queen's position from pos ",pos)
            Queen -= 1
            print("Again check prev Queen's\n")







n = 4
print(totalNQueens(n))
