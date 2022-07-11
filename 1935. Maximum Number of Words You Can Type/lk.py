  def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        lst=[]
        nw_lst=text.split()
        bk_lst=list(brokenLetters)
        for i in range(len(nw_lst)):
            count=0
            for j in range(len(bk_lst)):
                if(bk_lst[j] in nw_lst[i]):
                    count=count+1
                    break
            if(count==0):
                lst.append(nw_lst[i])
        return len(lst)
