class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}#dictionary
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1#create a dictionary to store the coccurence of the numbers
        for key,value in d.items():#iterate over the dictionary to check if the occurences of the number is more than half of the array length.
            print(key,value)
            if value>(len(nums)/2):#if true return the key ie number
                return key
    
