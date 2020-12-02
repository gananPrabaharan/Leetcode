from collections import deque


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messageSet = set()
        self.messageQueue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while len(self.messageQueue) > 0:
            earlyMessage, earlyTime = self.messageQueue[0]
            if earlyTime <= timestamp - 10:
                self.messageQueue.popleft()
                self.messageSet.remove(earlyMessage)
            else:
                break

        if message not in self.messageSet:
            self.messageQueue.append((message, timestamp))
            self.messageSet.add(message)
            return True

        return False
