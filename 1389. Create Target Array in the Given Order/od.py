class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in range(len(index)):
             lst.insert(index[i],nums[i])
        return lst
