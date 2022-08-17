class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}# create an empty dictionary 
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1#store the occurences of each character
        for i in range(len(s)):
            if d[s[i]] == 1:#return the first character's position according to the sentence in the dictionary with occurence one
                return i
        return -1
