class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        lst=[]
        for i in range(len(sentences)):
            ab = len(sentences[i].split())
            lst.append(ab)
        lst.sort()
        return lst[-1]
