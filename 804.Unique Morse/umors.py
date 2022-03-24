  class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            for j in range (len(nums)):# Traverse the list
              sum = nums[i]+ nums[j] #store sum
              if(sum == target): #compare value
                    return i,j #return indices
