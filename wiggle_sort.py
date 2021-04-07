class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        increasing = 1
        i = 1

        while i < len(nums):
            difference = nums[i] - nums[i - 1]

            if difference * increasing < 0:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp

            increasing *= -1
            i += 1
