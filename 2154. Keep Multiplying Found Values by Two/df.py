 temp=[]
        for i in nums:
            if(i%original==0):
                temp.append(i//original)
        i=1
        while i in temp:
            original*=2
            i*=2 
        return original
