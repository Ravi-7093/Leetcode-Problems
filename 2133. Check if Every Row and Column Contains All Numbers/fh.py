class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
       
        n = len(matrix)
        vaild = set(range(1, n + 1))
        #print(vaild)
        for i in range(n):
            set1, set2 = set(), set()
            for j in range(n):
                set1.add(matrix[i][j])
                set2.add(matrix[j][i])
            if set1 != vaild or set2 != vaild:
                return False
        return True
