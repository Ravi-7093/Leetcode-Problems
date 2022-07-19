class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        sum=0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for key,value in d.items():
            if value==1:
                sum =sum+key
        return sum
