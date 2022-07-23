import re


def minOperations(logs):  # solution 1
    distance = 0
    # regex for ../ is ^\.\.\/$
    # regex for ./ is ^\.\/$
    for i in logs:
        # print("\ni= ", i)
        if re.search("^\.\.\/$", i):
            # print(f"{i} found")
            # print("distance = ", distance)
            distance = distance - 1
            if distance < 0:
                distance = 0
            continue
            # print("distance = ", distance)
        elif re.search("^\.\/$", i):
            continue
        else:
            distance += 1
        # print("distance = ", distance)
    return distance


def minOperations2(logs):  # solution 2
    distance = 0
    # regex for ../ is ^\.\.\/$
    # regex for ./ is ^\.\/$
    for i in logs:
        # print("\ni= ", i)
        if i == "../":
            # print(f"{i} found")
            # print("distance = ", distance)
            distance = distance - 1
            if distance < 0:
                distance = 0
            continue
            # print("distance = ", distance)
        elif i == "./":
            continue
        else:
            distance += 1
        # print("distance = ", distance)
    return distance


logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
print(minOperations2(logs))
