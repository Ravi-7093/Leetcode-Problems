class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        lst=[]
        count=0
        for i in range(len(rectangles)):
            min_val=min(rectangles[i][0],rectangles[i][1])
            lst.append(min_val)
        lst.sort(reverse=True)
        max_ele=lst[0]
        for i in lst:
            if i==max_ele:
                count=count+1
        return count
