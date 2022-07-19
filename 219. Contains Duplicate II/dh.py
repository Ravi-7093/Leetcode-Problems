def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
       
        d={}
        for i,num in enumerate(nums):
            if num in d:
                if i-d[num]<=k:
                    return True
                else:
                    d[num]=i
            else:
                d[num]=i
        return False
