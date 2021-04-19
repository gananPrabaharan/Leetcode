class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        firstTwoSums = {}
        lastTwoSums = {}

        # Get all possible sums from first two lists
        for i in nums1:
            for j in nums2:
                pairSum = i + j
                firstTwoSums[pairSum] = firstTwoSums.get(pairSum, 0) + 1

        # Get all possible sums from last two lists
        for i in nums3:
            for j in nums4:
                pairSum = i + j
                lastTwoSums[pairSum] = lastTwoSums.get(pairSum, 0) + 1

        num4Sums = 0
        # Identify pairs from constructed dictionaries
        for leftSum, leftCount in firstTwoSums.items():
            rightSum = -1 * leftSum

            if rightSum in lastTwoSums:
                # Number of possibilities is the product of the two counts
                num4Sums += lastTwoSums[rightSum] * leftCount

        return num4Sums
