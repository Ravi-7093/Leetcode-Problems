class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        for i in range(len(items)):
            
            if(ruleKey=="color"):
                if(ruleValue==items[i][1]):
                    count=count+1
            elif(ruleKey=="type"):
                if(ruleValue==items[i][0]):
                    count=count+1
            else:
                if(ruleValue==items[i][2]):
                    count=count+1
        return count
