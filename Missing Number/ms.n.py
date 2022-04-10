 def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)+1): 
             if i not in nums: //if index not present in nums
                return i  // return num
