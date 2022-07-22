class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            count=0
            arr=nums[:i]+nums[i+1:]
            for j in range(1,len(arr)):
                if(arr[j]<=arr[j-1]):
                    break
                else:
                     count=count+1
            if(count==len(arr)-1):
                 return True
        return False
             
