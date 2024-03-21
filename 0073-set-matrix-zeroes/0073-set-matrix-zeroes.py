class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        m = len(matrix)     #no. of rows
        n = len(matrix[0])  #no. of columns
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        for i in rows:
            for p in range(n):
                matrix[i][p] =0
        for j in columns:
            for q in range(m):
                matrix[q][j] =0
        