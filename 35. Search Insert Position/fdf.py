class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_srch(nums,target,low,high):
            mid=(low+high)//2
            if(high>=low):
             #print(high,low)
               
                if(nums[mid]==target):
                        return mid
                elif(nums[mid]>target):
                        return binary_srch(nums,target,low,mid-1)
                else:
                         return binary_srch(nums,target,mid+1,high)
            else:
                 return mid+1
        res=binary_srch(nums,target,0,len(nums)-1)
        return res   
