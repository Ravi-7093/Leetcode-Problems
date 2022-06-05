class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res=0
        for x in operations:
            if(x.startswith("+") or x.endswith("+") ):
                res=res+1
            else:
                res=res-1
        return res
