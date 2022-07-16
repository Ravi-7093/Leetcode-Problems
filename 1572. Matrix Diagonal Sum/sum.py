class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum=0
        c=len(mat)//2
        for i in range(len(mat)):
           sum+=mat[i][i]
           sum+=mat[len(mat)-1-i][i]
        if(len(mat)%2==1):
            sum-=mat[c][c]
        return sum
