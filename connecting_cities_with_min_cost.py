class Solution:
    def __init__(self):
        self.vertexParent = {}

    def find(self, v):
        parent = self.vertexParent[v]
        if parent == v:
            return v
        self.vertexParent[v] = self.vertexParent[parent]
        return self.find(parent)

    def union(self, v1, v2):
        parent2 = self.find(v2)
        parent1 = self.find(v1)

        if parent2 == parent1:
            return False

        self.vertexParent[parent2] = self.vertexParent[parent1]
        return True

    def minimumCost(self, N, connections) -> int:
        if len(connections) < N - 1:
            return -1

        for i in range(1, N + 1):
            self.vertexParent[i] = i

        sortedConnections = sorted(connections, key=lambda x: x[2])

        totalCost = 0
        numEdges = 0
        for v1, v2, cost in sortedConnections:
            if self.union(v1, v2):
                numEdges += 1
                totalCost += cost

            if numEdges == N - 1:
                break

        parent = self.find(1)
        # Check that there are no disjoin sets
        for v, p in self.vertexParent.items():
            if self.find(p) != parent:
                return -1

        return totalCost
