class Solution:
    def reverse(self, nums, startIndex):
        if startIndex == len(nums) - 2:
            temp = nums[startIndex]
            nums[startIndex] = nums[len(nums) - 1]
            nums[len(nums) - 1] = temp
            return

        midIndex = startIndex + (len(nums) - startIndex) // 2
        for i in range(startIndex, midIndex):
            temp = nums[i]
            swapIndex = len(nums) - 1 - (i - startIndex)
            nums[i] = nums[swapIndex]
            nums[swapIndex] = temp

    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        startIndex = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                startIndex = i - 1
                break

        if startIndex is None:
            self.reverse(nums, 0)
            return

        swapIndex = -1
        for j in range(startIndex + 1, len(nums)):
            if nums[j] <= nums[startIndex]:
                swapIndex = j - 1
                break

        temp = nums[swapIndex]
        nums[swapIndex] = nums[startIndex]
        nums[startIndex] = temp
        self.reverse(nums, startIndex + 1)