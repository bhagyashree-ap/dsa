class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)

        #transpose
        for i in range(length):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #reverse each row
        for row in matrix:
            row.reverse()