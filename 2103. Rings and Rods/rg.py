class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        d={}
        count=0
        for i in range(0,len(rings),2):
            cr_rod=rings[i+1]
            cr_color=rings[i]
            if cr_rod in d:
                if cr_color in d[cr_rod]:
                    d[cr_rod].remove(cr_color)
                    if not d[cr_rod]:
                        count=count+1

            else:
                d[cr_rod]={'R','G','B'}
                d[cr_rod].remove(cr_color)
        return count
