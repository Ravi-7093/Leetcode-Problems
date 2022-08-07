class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        res=[]
        d={'(':')','{':'}','[':']'} #create a dictionary by pairing brackets
        for i in s:
            if i in d: #append the left bracket if in dictionary 
                res.append(i)
            else: 
                if len(res)==0 or d[res.pop()]!=i: #check if the left bracket has the value appropriate  closing bracket  
                    return False
        return len(res)==0 #return True
