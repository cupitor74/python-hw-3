def spiral(matrix):
    list = []
    if not matrix or not len(matrix):
        return
 
    top_index = left_index = 0
    bottom_index = len(matrix) - 1
    right_index = len(matrix[0]) - 1
 
    while True:
        if left_index > right_index:
            break

        for i in range(left_index, right_index + 1):
            list.append(matrix[top_index][i])
        top_index = top_index + 1
 
        if top_index > bottom_index:
            break
 
        for i in range(top_index, bottom_index + 1):
            list.append(matrix[i][right_index])
        right_index = right_index - 1
 
        if left_index > right_index:
            break
 
        for i in range(right_index, left_index - 1, -1):
            list.append(matrix[bottom_index][i])
        bottom_index = bottom_index - 1
 
        if top_index > bottom_index:
            break

        for i in range(bottom_index, top_index - 1, -1):
           list.append(matrix[i][left_index]) 
        left_index = left_index + 1
    return list
 
 
matrix = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9,10,11,12]]
matrix1 = [[1, 2, 3, 4, 5, 6],
            [7, 8, 9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30]]

print(spiral(matrix))
print(spiral(matrix1))