import numpy as np
matrix = np.array([ [1, 2, 3],
                    [4, 2, 0],
                    [1, 2, 3] ])

def checkRow(matrix, check):
    for sum in matrix.sum(axis = 0):
        if (sum != check): return False
    return True

def checkCol(matrix, check):
    for sum in matrix.sum(axis = 1):
        if (sum != check): return False
    return True

print(matrix)
if(matrix.shape[0]== matrix.shape[1]):

    row = matrix.shape[0]
    col = matrix.shape[1]

    sum_first_diagonal = sum(matrix[i][i] for i in range(row))
    sum_second_diagonal = sum(matrix[i][col - i - 1] for i in range(col))

    if((sum_first_diagonal == sum_second_diagonal) and checkRow(matrix, sum_first_diagonal) and checkCol(matrix, sum_first_diagonal)):
        print("Co la Matrix square")
    else:
        print("Khong la Matrix square")
else: print("Khong la Matrix square")





