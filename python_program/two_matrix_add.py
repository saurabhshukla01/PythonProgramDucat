# Python Program - Add Two Matrices



		
matrix1 = [[1, 2, 3],
		   [4, 5, 6],
	       [7, 8, 9]]
matrix2 = [[10, 11, 12],
	       [13, 14, 15],
	       [16, 17, 18]]
matrix =  [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0]]
			
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix[i][j] = matrix1[i][j] + matrix2[i][j]
for r in matrix:
    print(r)
	
	
	
'''

output ===

matrix1 = [[1, 2, 3],
		   [4, 5, 6],
	       [7, 8, 9]]
matrix2 = [[10, 11, 12],
	       [13, 14, 15],
	       [16, 17, 18]]

a+b ==	[11, 13, 15]
		[17, 19, 21]
		[23, 25, 27]
		
		
'''