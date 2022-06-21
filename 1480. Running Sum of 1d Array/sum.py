class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        lst=[]
        for i in range(len(nums)):
            sum=nums[i]+sum
            lst.append(sum)
        return lst
