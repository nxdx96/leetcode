class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dupe = set(nums)

        return len(dupe) != len(nums)