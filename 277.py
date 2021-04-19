# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        p1 = 0
        for p2 in range(1, n):
            if knows(p1, p2):
                # Take next candidate
                p1 = p2

        for i in range(n):
            if i == p1:
                continue

            # Make sure everyone knows p1, but p1 doesn't know anyone
            if knows(p1, i) or not knows(i, p1):
                return -1

        return p1
