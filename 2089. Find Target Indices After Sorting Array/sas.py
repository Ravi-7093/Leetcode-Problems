class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        lst=[]
        for i in range(len(nums)):
             if(nums[i]==target):
                    lst.append(i)
        return lst
