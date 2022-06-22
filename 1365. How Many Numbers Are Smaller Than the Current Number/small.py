class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if(nums[i]>nums[j] and j!=i):
                    count=count+1
            lst.append(count)
        return lst
