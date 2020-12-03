from collections import deque

class Solution:
    def findCircleNum(self, M):
        numCircles = 0
        visitedSet = set()

        # Initialize queue used to iterate through each friend circle
        friendCircleQueue = deque()

        # Iterate through all friends
        for i in range(len(M)):
            if i in visitedSet:
                # Already counted this individual
                continue

            # Mark person as visited and add them to our current queue
            visitedSet.add(i)
            friendCircleQueue.append(i)

            # Iteratively add all new friends to the friend circle Queue
            while len(friendCircleQueue) > 0:
                currPerson = friendCircleQueue.popleft()

                for j in range(len(M)):
                    # Add unvisited friends to queue and mark them as visited
                    if j not in visitedSet and M[currPerson][j] == 1:
                        visitedSet.add(j)
                        friendCircleQueue.append(j)

            numCircles += 1

        return numCircles
