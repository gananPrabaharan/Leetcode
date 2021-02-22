class Solution:
    def numWays2(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        if n < 3:
            return k ** n

        prevPost = k ** 2
        prevPrevPost = k
        for i in range(3, n + 1):
            currPost = (k - 1) * (prevPost + prevPrevPost)
            prevPrevPost = prevPost
            prevPost = currPost

        return currPost

    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        same = 0
        diff = k

        for i in range(2, n + 1):
            newSame = diff
            newDiff = (diff + same) * (k - 1)

            same = newSame
            diff = newDiff

        return same + diff
