class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        startIndex = 0
        letterDict = {}

        maxLength = 0
        for endIndex in range(len(s)):
            char = s[endIndex]
            letterDict[char] = letterDict.get(char, 0) + 1

            while len(letterDict.keys()) > k:
                startChar = s[startIndex]
                letterDict[startChar] -= 1

                if letterDict[startChar] == 0:
                    del letterDict[startChar]

                startIndex += 1
            maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength
