class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=""
        for i in range(len(s)-1,-1,-1):#reverse the string
	        if(s[i]==' ' and ans==""):#if whitespace continue
		            continue
	        elif(s[i]!=' '):#if a character is encountered
		             ans+=s[i] #add it to the result
	        else:
		         return(len(ans))
            
        if(len(ans)>0):
            return len(ans)#return the lenght of the result
        return 0
