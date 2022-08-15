class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {} #create an empty dictionary 
        start = 0 #first pointer 
        count=0 #counter tot track of valisd substrings of length K
        for i,f in enumerate(s):#enumerate in s 
            if f in d:#if f in d 
                start = max(start,d[f]+1) #get the pointer value updated after encountering an existing character ie move the window forward
                d[f]=i#append the latest value to the character 
            else:
                d[f]=i#append the values if no dictionary is found 
                print(d)
            if i-start + 1 == k: #check if the second pointer - first pointer results the specified size
                count += 1#increment counter 
                start += 1#increment the first pointer 
        return count
