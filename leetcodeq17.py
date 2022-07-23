def networkDelayTime(times, n, k):
    Flag = True
    Total_time = 0

    # if len(times) == 1 and times[0][0] == k and times[0][1] == n:
    #     return times[0][2]
    # elif (len(times) == 1 and times[0][0] == k and times[0][1] != n) or (len(times) == 1 and times[0][0] != k):
    #     print("Here")
    #     return -1

    for sublst in times:
        #print("sublst[0] = ", sublst[0][0])
        if sublst[0][0] is k:
            Flag = True
            break
        elif sublst[0][0] is not k:
            Flag = False
            continue

    if Flag == False:
        print("k not found")
        return -1

    def pathFinder(lst, tmp_k):
        curr_time = 0
        time = 0
        new_time = 0
        print("Begin ----")
        print("lst = ", lst)
        print("tmp_k = ", tmp_k)
        print("lst[0][0][0] = ", lst[0][0][0])
        print("lst[0][0][1] = ", lst[0][0][1])
        print("\nif lst[0][0][0] == tmp_k and lst[0][0][1] == n:")
        if lst[0][0][0] == tmp_k and lst[0][0][1] == n:
            print(True)
            print('Return current node time', lst[0][0][2])
            return lst[0][0][2]

        elif lst[0][0][0] == tmp_k and lst[0][0][1] != n:
            print("\nlst[0][0][0] == tmp_k and lst[0][0][1] != n:")
            print(True)
            curr_time = lst[0][0][2]
            try:
                print('time = ', time)
                new_time = pathFinder(lst[1:], lst[0][0][1])
            except:
                pass
        elif lst[0][0][0] != tmp_k:
            try:
                print('time = ', time)
                new_time = pathFinder(lst[1:], lst[0][0][1])
            except:
                pass
        time = new_time + curr_time
        print("Return Total Time = ", time)
        return time

    print("Call function")
    Total_time = pathFinder(times, k)

    return Total_time


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
n = 4
k = 2
print(networkDelayTime(times, n, k))
