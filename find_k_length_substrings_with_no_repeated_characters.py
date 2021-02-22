class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        numSubstrings = 0
        charDict = {}

        i = 0
        while i < len(S):
            currLetter = S[i]

            if currLetter not in charDict:
                charDict[currLetter] = i
            else:
                startIndex = charDict[currLetter] + 1
                charDict = {}
                for j in range(startIndex, i + 1):
                    charDict[S[j]] = j

            if len(charDict) == K:
                print(charDict)
                numSubstrings += 1
                del charDict[S[i - K + 1]]

            i += 1
        return numSubstrings
