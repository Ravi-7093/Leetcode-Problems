class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in range(len(s)):
            if s[i].isalpha():
                res+=s[i]
            else:
                c=ord(s[i-1])
            #print(c,s[i])
                c=c+int(s[i])
                res+=chr(c)
        return(res)
