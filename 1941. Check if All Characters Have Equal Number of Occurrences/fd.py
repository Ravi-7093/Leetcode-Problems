  def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={}
        for i in range(len(s)):
             d[s[i]]=d.get(s[i],0)+1
        val=d.get(s[0])
        for i in d:
            if(d.get(i)!=val):
                return False
        return True
