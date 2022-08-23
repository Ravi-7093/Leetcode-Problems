class Solution(object):
    def largestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        start=0 #using technique of sliding window and intializing the variables
        end=k-1#window size
        largest=0 #to store largest of the number 
        ans=[]#resultlist 
        while(end<len(nums)):#traverse until the window reaches the end of loop
            if(nums[start]>largest):#check if the current element is largest 
                largest=nums[start]#update the largest to the latest element
                ans=nums[start:end+1]#store the value in result arr 
            start+=1#traverse the loop  check if the next subarray is optimized
            end+=1
        return ans#return an empty list 
