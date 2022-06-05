class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        x=""
        for i in address:
            if (i=="."):
                x=address.replace(".","[.]")
                return x
