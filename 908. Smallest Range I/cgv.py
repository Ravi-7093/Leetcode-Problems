class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val=max(nums)
        min_val=min(nums)
        if(min_val+k >= max_val-k):
            return 0
        else:
            return (max_val-k) -(min_val+k)
