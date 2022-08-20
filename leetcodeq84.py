# 871. Minimum Number of Refueling Stops

def minRefuelStops(target, startFuel, stations):
    n = len(stations)
    stations.append([target, 0])
    heap = []
    cur_fuel = startFuel
    prev_pos, count = 0, 0

    for pos, fuel in stations:

        #decrement fuel to reach cur position
        cur_fuel -= (pos - prev_pos)

        #if it is negatives, that means we need to refuel in the prev stations
        #fill with the largest fuel we can have
        while cur_fuel<0:
            if not heap: return -1
            cur_fuel -= heappop(heap)
            count+=1

        #add fuel to the heap set that might be needed for future computation
        #the heap contains stations that we are not refuelling so far
        heappush(heap, -fuel)


        prev_pos = pos

    return count
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
print(minRefuelStops(target, startFuel, stations))
