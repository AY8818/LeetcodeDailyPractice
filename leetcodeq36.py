def timeRequiredToBuy(tickets, k):
    time_taken = 0
    while tickets[k] != 0:
        i = 0
        while i < len(tickets):
            if tickets[i] != 0 and tickets[k] != 0:
                tickets[i] = tickets[i] - 1
                time_taken += 1
            i = i + 1
    return time_taken


tickets = [84, 49, 5, 24, 70, 77, 87, 8]
k = 3
print(timeRequiredToBuy(tickets, k))
