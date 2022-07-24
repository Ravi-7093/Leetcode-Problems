class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid)):
                rows_max[i]=max(rows_max[i],grid[i][j])
                cols_max[j]=max(cols_max[j],grid[i][j])
        res=0
        for i in range(len(grid)):
             for j in range(len(grid)):
                res+=min(rows_max[i],cols_max[j])-grid[i][j]
        return res
