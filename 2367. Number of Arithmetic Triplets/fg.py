class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count=0#Intialize the counter to zero
        for i in range(len(nums)):#Travere through each element
            for j in range(i+1,len(nums)):#
                for k in range(j+1,len(nums)):
                    if(i<j<k) and (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):#check if i<j<k and validate the conditions.
                            count+=1# Update the counter if the condition staisfies
        return count#return the counter
