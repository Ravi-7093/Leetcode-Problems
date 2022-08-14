class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lst_one=[]#list_one empty 
        lst_two=[]#list_two empty 
        lst_three=[]#list_three empty 
        res=[]
        for i in range(len(nums)):#nums
            if(nums[i]<pivot):#if nums[i]<pivot
                lst_one.append(nums[i])#append values to first list
            elif(nums[i]==pivot):#if nums[i]==pivot
                lst_two.append(nums[i])#append values to second list
            else:
                lst_three.append(nums[i])#append values to third list
        res=lst_one+lst_two+lst_three#return  res
        return res
