arr = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# Solution is to work backwards through the tree, calculating the maximum of each node as you go
# Replce the node with the max value of the two child nodes + the node
def find_max_path(arr):
    rowcount = len(arr)-1
    for row,values in enumerate(arr):
        row_from_end = rowcount-row
        values = arr[row_from_end]
        if row_from_end == rowcount:
            continue
        for i,val in enumerate(values):
            values[i] = val  + max(arr[row_from_end+1][i], arr[row_from_end+1][i+1])
            print(i)
    return arr[0][0]

print(find_max_path(arr))
                
