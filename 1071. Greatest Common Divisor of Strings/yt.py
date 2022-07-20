class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n1 =len(str1)
        n2 = len(str2)
        if(str1==str2):
            return str1
        if(str1+str2 !=str2+str1):
            return ""
        def gcd(n1,n2):
            while(n2):
                n1,n2 = n2,n1%n2
            return n1
        len_gcd = gcd(n1, n2)
        #print(len_gcd)
        if str1[:len_gcd] == str2[:len_gcd]:
            return str1[:len_gcd]
        else:
            return ""
