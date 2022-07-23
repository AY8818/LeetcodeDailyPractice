def mergeTwoLists(list1, list2):
    list1 = list1 + list2
    list1.sort()
    print(list1)


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(mergeTwoLists(list1, list2))
