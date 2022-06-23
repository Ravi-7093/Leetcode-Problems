class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(arr)):
            count=0
            new_sum=0
            for j in range(i,len(arr)):
                new_sum+=arr[j]
                if((count+1)%2==1):
                    total+=new_sum
                count+=1
        return total
            
