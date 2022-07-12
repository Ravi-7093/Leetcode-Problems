class Solution(object):
    def truncateSentence(self, s, k):
        
        res=" "
        s=s.split()
        for i in range(0,k):
            res=res+' '+s[i]
        return(res.strip())
