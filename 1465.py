class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        # Go through horizontal cuts in sorted order, and then identify largest section as this defines heights of pieces
        # we know largest piece will be in this section since vertical cuts will only change widths of pieces

        horizontalCuts.sort()
        verticalCuts.sort()

        prevCut = 0
        maxHeight = 0
        for cut in horizontalCuts:
            maxHeight = max(maxHeight, cut - prevCut)
            prevCut = cut

        maxHeight = max(maxHeight, h - prevCut)

        prevCut = 0
        maxWidth = 0
        for cut in verticalCuts:
            maxWidth = max(maxWidth, cut - prevCut)
            prevCut = cut

        maxWidth = max(maxWidth, w - prevCut)

        maxArea = maxWidth % (10 ** 9 + 7) * maxHeight % (10 ** 9 + 7)
        return maxArea
