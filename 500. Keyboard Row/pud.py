class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first=set("qwertyuiop")
        second=set("asdfghjkl")
        third= set("zxcvbnm")
        d={}
        result=[]
        for i in range(97,123):
            count=0
            if(chr(i) in first):
                count=1
            elif(chr(i) in second):
                 count=2
            else:
                 count=3
            d[chr(i)]=count
        for word in words:
            lwr = word.lower()
            count=set()
            for i in lwr:
                count.add(d[i])
            if(len(count)==1):
                result.append(word)
        return result
