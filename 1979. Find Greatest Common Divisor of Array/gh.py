class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        large=nums[0]
        small=nums[-1]
        while(large):
            small, large= large, small % large
        return small
