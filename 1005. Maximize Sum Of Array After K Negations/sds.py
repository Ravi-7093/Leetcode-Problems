class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] < 0 and k > 0:
            k -= 1
            nums[i] *= -1
            i += 1
        if k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - 2*min(nums)
                
