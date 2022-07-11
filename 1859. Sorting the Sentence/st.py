class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s=s.split()
        d={}
        res=""
        for i in range(len(s)):
            d[s[i][-1]]=s[i]
        for key in sorted(d.keys()):
            word=d[key]
            res=res+(word[:-1])+" "
        return res.strip()
