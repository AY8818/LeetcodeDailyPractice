def NestedIterator(nestedList):
    print(nestedList)
    tem = nestedList
    newlst = []
    Flag = False

    while True:
        if len(tem) == 0:
            break
        element = next(tem)
        Flag = hasNext(element)
        if Flag == True:
            pass
        else:
            print("False")
            newlst.append(element)
            continue

    return(newlst)


def flatter(lst):
    pass


def next(lst):
    return lst.pop(0)


def hasNext(element):
    if type(element) is list:
        return True
    elif type(element) is int:
        return False


nestedList = [1, [4, [6]]]
print(NestedIterator(nestedList))
