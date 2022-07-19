class Solution(object):
    def divideArray(self, nums):
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for key,value in d.items():
              if(value%2!=0):
                     return False
        return True
