# 812. Largest Triangle Area
def largestTriangleArea(points):
    #(ΔABC) = (1/2)(x1*(y2 − y3) + x2*(y3 − y1) + x3*(y1 − y2))
    largest_area = 0
    length = len(points)
    for i in range(length):
        x1, y1 = points[i]
        # print("i = ",points[i])
        for j in range(i + 1, length):
            x2, y2 = points[j]
            # print("j = ",points[j])
            for k in range(j + 1, length):
                x3, y3 = points[k]
                # print("k = ",points[k])
                curr_area = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                if curr_area > largest_area:
                    largest_area = curr_area
    return largest_area


points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
print(largestTriangleArea(points))
