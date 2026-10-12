class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for i in range(len(nums)):
            x = nums[i]
            needed = target - x

            if needed in seen:
                return [seen[needed], i]

            seen[x] = i