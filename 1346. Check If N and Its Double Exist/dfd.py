def checkIfExist(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 2:
            return False
        d={}
        for i in arr:
            if i in d:
                return True
            d[i*2]= True
            d[i/2]=True
        return False
