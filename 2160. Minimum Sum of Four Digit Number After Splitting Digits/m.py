class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
       
        lst=list(str(num))
        lst.sort()
        #print(lst)
        res=0
        #print(lst[0])
        res=int(lst[0])*10+int(lst[1])*10+int(lst[2])+int(lst[3])
        return res
