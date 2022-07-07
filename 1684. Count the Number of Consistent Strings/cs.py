class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for word in words:
            for i in word:
                 if(i not in allowed):
                        break
            else:
                count=count+1
        return count
        
