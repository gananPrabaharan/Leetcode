from heapq import heappush, heappop


class Node:
    def __init__(self, val, prevNode=None, nextNode=None):
        self.val = val
        self.prev = prevNode
        self.next = nextNode

    def removeNode(self):
        if self.prev is not None:
            self.prev.next = self.next

        if self.next is not None:
            self.next.prev = self.prev


class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.recentNode = None
        self.nodeDict = {}
        self.maxHeap = []

    def push(self, x: int) -> None:
        currNode = Node(x)

        if self.recentNode is not None:
            self.recentNode.next = currNode
            currNode.prev = self.recentNode

        self.recentNode = currNode

        if x in self.nodeDict:
            self.nodeDict[x].append(currNode)
        else:
            self.nodeDict[x] = [currNode]
            heappush(self.maxHeap, -x)

    def pop(self) -> int:
        popNode = self.recentNode

        if popNode is not None:
            self.recentNode = popNode.prev
            popNode.removeNode()

            popVal = popNode.val
            self.nodeDict[popVal].pop()

            if len(self.nodeDict[popVal]) == 0:
                del self.nodeDict[popVal]

            return popVal

        return None

    def top(self) -> int:
        if self.recentNode is None:
            return None
        return self.recentNode.val

    def peekMax(self) -> int:
        if self.recentNode is None:
            return None

        while -self.maxHeap[0] not in self.nodeDict:
            heappop(self.maxHeap)

        return -self.maxHeap[0]

    def popMax(self) -> int:
        maxVal = self.peekMax()

        if maxVal is not None:
            maxNode = self.nodeDict[maxVal].pop()

            if len(self.nodeDict[maxVal]) == 0:
                del self.nodeDict[maxVal]
                heappop(self.maxHeap)

            if maxNode == self.recentNode:
                self.recentNode = maxNode.prev

            maxNode.removeNode()

        return maxVal
