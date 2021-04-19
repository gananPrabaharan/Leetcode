class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        startIndex = 1
        endIndex = len(nums) - 1

        while startIndex != endIndex:
            midIndex = (startIndex + endIndex) // 2
            if nums[midIndex] < nums[midIndex - 1]:
                endIndex = midIndex - 1
            elif nums[midIndex] < nums[midIndex + 1]:
                startIndex = midIndex + 1
            else:
                return midIndex

        return startIndex
