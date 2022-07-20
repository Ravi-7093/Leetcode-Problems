class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        count=0
        p=0
        lst=[]
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for key, value in d.items():
            if(value%2==0):
                p+=value//2
            else:
                p+=value//2
                count+=1
           
        return [p,count]
