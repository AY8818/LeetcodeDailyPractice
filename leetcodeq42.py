import bisect


def maxEnvelopes(envelopes):
    lst = []
    for _, i in sorted(envelopes, key=lambda e: (e[0], -e[1])):
        try:
            lst[bisect.bisect_left(lst, i)] = i
        except IndexError:
            lst.append(i)
    return len(lst)


envelopes = [[1, 2], [2, 3], [3, 4], [3, 5], [4, 5], [5, 5], [5, 6], [6, 7], [7, 8]]

e = [[5, 4], [6, 4], [6, 7], [2, 3]]
e2 = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]

e3 = [[1, 1], [1, 1], [1, 1]]
print(maxEnvelopes(e2))
# len_of_env = len(envelopes)
#     lenti = []
#     widti = []
#     # last_inserted_val = 0
#     for i in envelopes:
#         lenti.append(i[0])
#         lenti.sort()
#         # print(f"\nif {i[0]} == {last_inserted_val}:{i[0] == last_inserted_val}                                           ")
#         # if i[0] == last_inserted_val:
#         #     indx = lenti.index(i[0]) + 1
#         # else:
#         indx = lenti.index(i[0])
#         widti.insert(indx, i[1])
#         # last_inserted_val = i[0]
#     print(lenti)
#     # print(widti)
#     for i in lenti:
#         cnt = lenti.count(i)
#         if cnt > 1:
#             idx = lenti.index(i)
#             lst = widti[idx:idx + cnt]
#             lst.sort()
#             for c in range(cnt):
#                 widti[idx] = lst[c]
#                 idx = idx + 1
#     print(widti)

#     env_count = 1
#     last_env_index = 0
#     temp = [[lenti[0], widti[0]]]
#     for i in range(1, len(lenti)):
#         # print("i=", i)
#         # print(f"if ({lenti[last_env_index]} < {lenti[i]}) and ({widti[last_env_index]} < {widti[i]}):")
#         if (lenti[last_env_index] < lenti[i]) and (widti[last_env_index] < widti[i]):
#             # print(True)
#             env_count += 1
#             last_env_index = i
#             temp.append([lenti[i], widti[i]])
#     print("temp = ", temp)

#     return env_count
