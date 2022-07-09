class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d={}
        for i in range(len(sentence)):
            d[sentence[i]]=d.get(sentence[i],0)+1
        if(len(d)==26):
            return True
        else:
            return False
