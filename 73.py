class Solution:
    @staticmethod
    def checkZeroRow(row):
        for x in row:
            if x == 0:
                return True
        return False

    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None

        m = len(matrix)
        n = len(matrix[0])

        # Flag indicating whether previous row needs to be converted to zeros
        prevRowZero = self.checkZeroRow(matrix[0])

        # Set rows with indices [0, n-2] to 0 if necessary
        # Cascade zeros down vertically (column-wise)
        for i in range(1, m):
            # Flag indicating whether previous row needs to be converted to zeros
            currRowZero = self.checkZeroRow(matrix[i])
            for j in range(n):
                # Adopt zeros from previous row
                if matrix[i - 1][j] == 0:
                    matrix[i][j] = 0

                # Set previous row value to zero if necessary
                elif prevRowZero:
                    matrix[i - 1][j] = 0
            prevRowZero = currRowZero

        # Cascade zeros up vertically (column-wise)
        for i in range(m):
            for j in range(n):
                if matrix[-1][j] == 0:
                    matrix[i][j] = 0

        # Set last row to zeros if necessary
        if prevRowZero:
            for j in range(n):
                matrix[-1][j] = 0
