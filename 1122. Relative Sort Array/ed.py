class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        lst_stor=[0]*(1001)
        for n in arr1:
            lst_stor[n]+=1
        res=[]
        for n in arr2:
            res+=lst_stor[n] * [n]
            lst_stor[n]=0
        for i,n in enumerate(lst_stor):
            if n:
                res+=(n*[i])
        return res
        
