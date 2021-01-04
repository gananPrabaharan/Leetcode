class Solution:
    def leastInterval(self, tasks, n):
        numTasks = len(tasks)

        frequencies = [0] * 26
        max_freq = 0
        num_max = 0

        for task in tasks:
            index = ord(task) - ord("A")
            frequencies[index] += 1
            if frequencies[index] > max_freq:
                max_freq = frequencies[index]
                num_max = 1
            elif frequencies[index] == max_freq:
                num_max += 1

        potentialIntervals = (n + 1) * (max_freq - 1) + num_max
        return max(potentialIntervals, numTasks)
