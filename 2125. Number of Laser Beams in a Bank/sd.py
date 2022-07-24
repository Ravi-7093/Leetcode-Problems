class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev_count=0
        total=0
        for i in range(len(bank)):
            count=0
            for j in bank[i]:
                if(int(j)==1):
                    count=count+1
            if(count>0):
                total+=(count*prev_count)
                prev_count=count
        return total
