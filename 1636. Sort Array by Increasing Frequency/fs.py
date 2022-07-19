def frequencySort():
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        #print(nums)
        d=dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+= 1
        #print(d)
        d=(sorted(d.items(), key= lambda x:x[1]))
        print(d)
        res=[]
        for i,j in d:
            print(i,j)
            for k in range(j):
                res.append(i)

        return res
