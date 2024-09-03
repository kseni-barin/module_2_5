def get_matrix(n, m, value):
    matrix = []
    if n > 0 and m > 0 and value > 0:
        for i in range(n):
            list = []
            for j in range(m):
                list.append(value)
            matrix.append(list)
        return matrix
    else:
        return matrix

matrix = get_matrix(4, 3, 1)
print(matrix)
#print(*matrix,sep = '\n')

