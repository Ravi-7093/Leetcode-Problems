class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        odd_lst=[]
        evn_lst=[]
        res=[]
        for i in range(len(nums)):
            if(nums[i]<0):
                odd_lst.append(nums[i])
            else:
                evn_lst.append(nums[i])
        res = [item for sublist in zip(evn_lst, odd_lst) for item in sublist]
        return res
