class Solution:
    @staticmethod
    def vectorMult(rowVec, colVec):
        rowIndex, colIndex, product = 0, 0, 0
        while rowIndex < len(rowVec) and colIndex < len(colVec):
            j, rowVal = rowVec[rowIndex]
            i, colVal = colVec[colIndex]

            if j < i:
                rowIndex += 1
            elif i < j:
                colIndex += 1
            else:
                product += rowVal * colVal
                rowIndex += 1
                colIndex += 1

        return product

    def multiply(self, mat1, mat2):
        n, m, k = len(mat1), len(mat1[0]), len(mat2[0])
        rowVectors = []
        for i in range(n):
            currRow = []
            for j in range(m):
                if mat1[i][j] != 0:
                    currRow.append((j, mat1[i][j]))
            rowVectors.append(currRow)

        colVectors = []
        for j in range(k):
            currCol = []
            for i in range(m):
                if mat2[i][j] != 0:
                    currCol.append((i, mat2[i][j]))
            colVectors.append(currCol)

        mat3 = []
        for i in range(n):
            currRow = []
            for j in range(k):
                product = self.vectorMult(rowVectors[i], colVectors[j])
                currRow.append(product)
            mat3.append(currRow)

        return mat3
