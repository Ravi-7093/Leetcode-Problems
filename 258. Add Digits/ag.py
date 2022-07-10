class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num>9):
            num_1=num%10
            #print(num_1)
            num_2=int(num/10)
            #print(num_2)
            sum=num_1+num_2
            num=sum
        return num
