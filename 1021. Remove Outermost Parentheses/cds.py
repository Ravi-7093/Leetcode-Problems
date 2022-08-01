class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        ans=""
        for i in range(len(s)):
            if not stack:
                    if s[i]=="(":
                        stack.append(s[i])
            else:
                    if s[i]=='(':
                        stack.append(s[i])
                        ans+=s[i]
                    else:
                        stack.pop()
                        if stack:
                            ans+=s[i]
                    
        return ans
