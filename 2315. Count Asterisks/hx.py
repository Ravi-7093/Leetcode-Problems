class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        s=s.split("|")
        for i in range(0,len(s),2):
            for j in s[i]:
                if j=="*":
                    count+=1
        return count
