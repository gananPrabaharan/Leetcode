class Solution:
    def isAlienSorted(self, words, order):
        if len(words) < 2:
            return True

        letterOrderDict = {}

        for index, letter in enumerate(order):
            letterOrderDict[letter] = index

        prevWord = words[0]
        for wordIndex in range(1, len(words)):
            currWord = words[wordIndex]
            comparisonLength = min(len(currWord), len(prevWord))

            for i in range(comparisonLength):
                prevLetter = prevWord[i]
                currLetter = currWord[i]

                prevIndex = letterOrderDict[prevLetter]
                currIndex = letterOrderDict[currLetter]

                if prevIndex > currIndex:
                    return False
                elif prevIndex < currIndex:
                    break
                elif i == comparisonLength - 1:
                    if len(prevWord) > len(currWord):
                        return False

            prevWord = currWord

        return True
