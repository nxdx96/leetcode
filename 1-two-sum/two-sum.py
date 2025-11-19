class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for n in range(len(nums)):
            diff = target - nums[n]
            for m in range(1, len(nums)):
                if diff == nums[m] and n != m:
                    return [n,m]

