import heapq


class Solution:
    @staticmethod
    def calcProfit(ballsPerColour, initialPrice, maxColours):
        nextPrice = initialPrice - ballsPerColour
        profit = initialPrice * (initialPrice + 1) // 2 - nextPrice * (nextPrice + 1) // 2
        return profit * maxColours, nextPrice

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # Create maxheap containing number of balls for each color
        ballHeap = [-b for b in inventory]
        heapq.heapify(ballHeap)
        maxProfit = 0

        # Pop off max value and reduce number of balls to next maxValue-1
        # Repeat above until order number of valls is achieved
        maxColours = 0
        while orders > 0:
            maxPrice = -heapq.heappop(ballHeap)
            if len(ballHeap) > 0:
                nextMax = -ballHeap[0]
            else:
                nextMax = 0
            maxColours += 1

            difference = maxPrice - nextMax
            sellBalls = difference * maxColours

            if sellBalls > orders:
                ballsPerColor = orders // maxColours
            else:
                ballsPerColor = difference

            profit, nextPrice = Solution.calcProfit(ballsPerColor, maxPrice, maxColours)

            if sellBalls > orders:
                nextSell = orders % maxColours
                maxProfit += nextPrice * (nextSell)

            maxProfit += profit
            orders -= sellBalls

        return maxProfit % (10 ** 9 + 7)
