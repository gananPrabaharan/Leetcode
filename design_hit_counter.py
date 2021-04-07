from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.total = 0
        self.hits = deque([])
        self.prevTimeStamp = -1

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.prevTimeStamp != timestamp:
            self.hits.append((timestamp, 1))
        else:
            self.hits[-1][1] += 1

        self.total += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.hits) > 0:
            if self.hits[0][0] <= timestamp - 300:
                ts, ts_hit = self.hits.popleft()
                self.total -= ts_hit
            else:
                break

        return self.total

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
