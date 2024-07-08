def matrixRotation ():
    
    m, n, r = [int(x) for x in input().split()]
    
    matrix = []
    
    # 1,2,3,4    5,6,7,8      9,10,11,12    13,14,15,16
    # 2,3,4,8    1,7,11,12    5,6,10,16     9,13,14,15
    # 3,4,8,12   2,11,10,16   1,7,6,5       5,9,13,14
    
    for _ in range(m):
        matrix.append([int(x) for x in input().split()])
    
    
    for _ in range(1):
        leftOver = []
        for i in range(len(matrix)): 
            for j in range(len(matrix[i])):
                if j == 0:
                    leftOver.append(matrix[i][j])
                    del matrix[i][j]

        for i in range(len(matrix)-1):
            matrix[i].append(matrix[i+1][2])
        
           
                
                    
                    
                
    print(matrix)
    
matrixRotation()