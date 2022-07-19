class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
            if(d[nums[i]]>1):
                return True
        return False
