from typing import List

matrix_size = int(input("Enter matrix size: "))

input_matrix : List = []

for column_no in range(matrix_size):
    matrix_rows : int = input().split(',')
    input_matrix.append(list(map(int, matrix_rows)))

transporse_matrix : List = []

for i in range(len(input_matrix)):
    transporse_row : List = []
    for j in range(len(input_matrix)):
        transporse_row.append(input_matrix[j][i])
    transporse_matrix.append(transporse_row)

multiplication_matrix : List =  [[0 for i in range(len(input_matrix))] for j in range(len(input_matrix))]


for i in range(len(input_matrix)):

    for j in range(len(input_matrix)):

        for k in range(len(input_matrix)):

            multiplication_matrix[i][j] += input_matrix[i][k] * transporse_matrix[k][j]


print('\n')

for row in multiplication_matrix:
    print(''.join(str(row)[1:-1].split(',')))



