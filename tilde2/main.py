import sys

# For testing predefined coordinates
# edge_list = [[5, 10],
#              [15, 20],
#              [20, 7]]
# edge_list = [[5, 10],
#              [20, 7],
#              [15, 20]]
# edge_list = [[4, 3],
#              [3, 3],
#              [3, 5],
#              [6, 5],
#              [6, 3],
#              [5, 3],
#              [5, 2],
#              [7, 2],
#              [7, 6],
#              [2, 6],
#              [2, 2],
#              [4, 2]]


# data input
coordinate_count = input("How many coordinates are you going to insert?\n")
try:
    coordinate_count = int(coordinate_count)
except:
    print("Entered value is not an integer")
    sys.exit()

edge_list = []
for i in range(coordinate_count):
    x = input(str(i + 1) + ". Coordinates x value\n")
    y = input(str(i + 1) + ". Coordinates y value\n")
    edge_list.append([int(x), int(y)])
print("Entered coordinates:", edge_list)


# figure calculation
sum = 0
# for all coordinates apply (x2 − x1)(y2 + y1)
for x in range(len(edge_list)):
    if not (x + 1 > len(edge_list) - 1):
        sum = sum + ((edge_list[x + 1][0] - edge_list[x][0]) * (edge_list[x + 1][1] + edge_list[x][1]))
    else:
        sum = sum + ((edge_list[0][0] - edge_list[x][0]) * (edge_list[0][1] + edge_list[x][1]))
        break


# result output
if sum > 0:
    print("Figure is clockwise")
elif sum < 0:
    print("Figure is counterclockwise")
elif sum == 0:
    print("Figure is colinear")
else:
    print("something went wrong")
