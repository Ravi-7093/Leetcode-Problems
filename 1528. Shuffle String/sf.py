class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res=""
        lst = list(s.strip(""))
        d={}
        for i in range(len(indices)):
            d[indices[i]]=lst[i]
        get_key=d.items()
        new_d=sorted(get_key)
        for i in range(len(new_d)):
            res+=new_d[i][1]
        return res
