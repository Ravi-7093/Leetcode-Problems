class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in range(1,len(nums),2):
            itr=nums[i-1]
            lst += [nums[i]] * itr  
        return lst
