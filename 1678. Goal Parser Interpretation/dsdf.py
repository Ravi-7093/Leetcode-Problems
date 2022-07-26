class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res=[]
        stack=[]
        for e in command:
            if e=="G":
                res.append("G")
            elif e ==")":
                if stack[-1]=="(":
                    res.append("o")
                else:
                    res.append("al")
                    stack=[]
            else:
                 stack.append(e)
        return "".join(res)  
