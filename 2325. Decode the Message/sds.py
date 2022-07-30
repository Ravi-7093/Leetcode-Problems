class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """   
        d={}
        j=0
        res=""
        s="abcdefghijklmnopqrstuvwxyz"
        key=key.replace(' ','')
        #print(key)
        for i in range(len(key)):
            if key[i] not in d:
                d[key[i]]=s[j]
                j=j+1
        for i in range(len(message)):
            if(message[i]==" "):
                res=res+" "
            else:
                res+=d[message[i]]
        return res
