class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_map:
                return [diff_map[diff], i]
            diff_map[n] = i

