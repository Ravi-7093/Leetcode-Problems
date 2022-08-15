class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0#First pointer
        count=0#increment is zero
        d={}#empty dicitonary
        for end,y in enumerate(s):#iterate the string
            if y in d:#if y in d 
                start=max(start,d[y]+1)#if value is already present update start pointer to move the window
                d[y]=end# update the value of dictionary
            else:
                d[y]=end#update the dictionary 
            if end-start+1 ==3:#check for window size. if present then increment pointers
                count+=1#increment counter
                start+=1#increment the start pointer
        return count
