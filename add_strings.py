class Solution:
    @staticmethod
    def stringToInt(s):
        return ord(s) - ord('0')

    def addStrings(self, num1: str, num2: str) -> str:
        index1 = len(num1) - 1
        index2 = len(num2) - 1

        sumString = ""
        q = 0

        while index1 >= 0 or index2 >= 0:
            currSum = q
            if index1 >= 0:
                currSum += self.stringToInt(num1[index1])
            if index2 >= 0:
                currSum += self.stringToInt(num2[index2])

            q, mod = divmod(currSum, 10)

            sumString = str(mod) + sumString

            index1 -= 1
            index2 -= 1

        if q > 0:
            sumString = str(q) + sumString

        return sumString