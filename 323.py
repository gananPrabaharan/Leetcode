from collections import deque

# 323. Number of Connected Components in an Undirected Graph


class Solution:
    def __init__(self):
        self.parentMap = {}
        self.rank = {}

    def find(self, val):
        parent = self.parentMap[val]
        if parent == val:
            return val

        self.parentMap[val] = self.find(parent)
        return self.parentMap[val]

    def union(self, val1, val2):
        parent1 = self.find(val1)
        parent2 = self.find(val2)

        if self.rank[parent1] < self.rank[parent2]:
            self.parentMap[parent1] = parent2
        else:
            self.parentMap[parent2] = parent1
            if self.rank[parent1] == self.rank[parent2]:
                self.rank[parent1] += 1

    def countComponents(self, n: int, edges) -> int:
        for i in range(n):
            self.parentMap[i] = i
            self.rank[i] = 0

        for n1, n2 in edges:
            self.union(n1, n2)

        parents = set()
        for n in self.parentMap.keys():
            parents.add(self.find(n))

        return len(parents)

    def countComponentsBFS(self, n: int, edges) -> int:
        connectedDict = {}
        unvisitedNodes = set()

        for i in range(n):
            connectedDict[i] = set()
            unvisitedNodes.add(i)

        for n1, n2 in edges:
            connectedDict[n1].add(n2)
            connectedDict[n2].add(n1)

        numComponents = 0
        completedNodes = set()
        for i in range(n):
            # while len(unvisitedNodes) > 0:
            if i not in unvisitedNodes:
                continue

            numComponents += 1
            nodeQueue = deque([i])

            while len(nodeQueue) > 0:
                currNode = nodeQueue.popleft()
                if currNode not in unvisitedNodes:
                    continue

                unvisitedNodes.remove(currNode)
                for connectedNode in connectedDict[currNode]:
                    if connectedNode in unvisitedNodes:
                        nodeQueue.append(connectedNode)

        return numComponents
