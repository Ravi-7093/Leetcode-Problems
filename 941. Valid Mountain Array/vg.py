class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        n=len(arr)
        new_point=0
        new_point_two=n-1
        for i in range(n-1):
            if(arr[i+1])==(arr[i]):
                return False
            else:
                if(arr[i+1]<arr[i]):
                    new_point=i
                    break
        for i in range(n-1,-1,-1):
            if(arr[i-1])==(arr[i]):
                return False
            else:
                if(arr[i-1]<=arr[i]):
                    new_point_two=i
                    break
        if (new_point==new_point_two) and new_point!=0 and new_point_two!=n-1:
            return True
