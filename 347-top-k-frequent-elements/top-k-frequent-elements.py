class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            nums_map[n] = 1 + nums_map.get(n, 0)
        
        for n, c in nums_map.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
