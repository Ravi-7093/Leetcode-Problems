class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range(len(grid)):
            for j in grid[i]:
                if(j<0):
                    count=count+1
        return count
