class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        for i in range(len(nums)):
            val = nums[nums[i]]
            arr.append(val)
        return arr
