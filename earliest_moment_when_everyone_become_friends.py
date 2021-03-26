class Solution:
    def __init__(self):
        self.friendDict = {}
        self.remainingPeople = 0

    def find(self, num):
        parent = self.friendDict[num]
        if parent == num:
            return num
        return self.find(parent)

    def union(self, num1, num2):
        parent1 = self.find(num1)
        parent2 = self.find(num2)

        if parent1 != parent2:
            self.friendDict[parent2] = parent1
            return True
        return False

    def earliestAcq(self, logs, N) -> int:
        if len(logs) < N - 1:
            return -1

        logs = sorted(logs, key=lambda x: x[0])

        for i in range(N):
            self.friendDict[i] = i

        self.remainingPeople = N - 1

        for timestamp, p1, p2 in logs:
            newAssociate = self.union(p1, p2)
            if newAssociate:
                self.remainingPeople -= 1
                if self.remainingPeople == 0:
                    return timestamp

        return -1