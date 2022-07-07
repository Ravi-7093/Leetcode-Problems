class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        lst=sentence.split(" ")
        ls=[]
        for i in range(len(lst)):
            if(lst[i].startswith(searchWord)):
                    ls.append(i+1)
        ls.sort()
        if(len(ls)!=0):
             return ls[0]
        else:
             return -1
