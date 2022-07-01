class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        total=0
        count=0
        sub=0

        boxTypes.sort(key = lambda x: x[1],reverse=True)
        for i in range(len(boxTypes)):
            total=boxTypes[i][0]*boxTypes[i][1]+total
            count=count+boxTypes[i][0]
            sub = truckSize-count
            if(count>truckSize):
                sub = count-truckSize
                total=total-boxTypes[i][1]*sub
                return total
        return total
