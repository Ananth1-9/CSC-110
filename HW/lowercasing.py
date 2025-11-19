def lowercase_items(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[r][c].lower()
            
    return matrix