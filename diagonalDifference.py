def diagonalDifference (n:int):

    """

    123 
    233 
    234

    321
    332
    432

    first_diaggonal = matrix[0][0], matrix [1][1], matrix [2][2]
    second_diaggonal = matrix[0][2], matrix [1][1], matrix [2][0]

    2344
    3455
    5676
    2347

    first_diagonal = matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]

    """

    matrix = []

    for i in range(n):
        matrix.append([int(x) for x in input().split()])

    left_diagonal = 0
    right_diagonal = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                left_diagonal+= matrix[i][j]
            
    reverse_matrix = []

    for i in range(n):
        matrix_im = matrix[i] 
        reverse_matrix.append(matrix_im[::-1])
    
    for i in range(n):
        for j in range(n):
            if i == j:
                right_diagonal += reverse_matrix[i][j]
    
    print(abs(left_diagonal-right_diagonal))




diagonalDifference(int(input()))