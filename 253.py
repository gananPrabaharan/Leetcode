import heapq


class MeetingNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, n2):
        return self.end < n2.end


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if len(intervals) < 2:
            return len(intervals)

        # Turn intervals into Nodes and sort them based of starting time
        nodeList = [MeetingNode(i[0], i[1]) for i in intervals]
        nodeList.sort(key=lambda x: x.start)

        # Create min-heap based off end time (determines which meeting will end next and free up a room)
        nodeHeap = [nodeList[0]]
        numRooms = 1
        availableRooms = 0
        for i in range(1, len(nodeList)):
            node = nodeList[i]

            # Clear off all meetings that will end before the next meeting starts
            # Assume it's fine if one meeting ends at the same time another one starts
            while len(nodeHeap) > 0 and node.start >= nodeHeap[0].end:
                heapq.heappop(nodeHeap)
                availableRooms += 1

            # If available rooms exist, use those, otherwise create a new room
            if availableRooms > 0:
                availableRooms -= 1
            else:
                numRooms += 1

            # Add the meeting to our heap
            heapq.heappush(nodeHeap, node)

        return numRooms
