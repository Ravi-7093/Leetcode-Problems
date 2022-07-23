class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        sum_s=0
        diff=0
        for i in range(len(seats)):
            diff=abs(seats[i]-students[i])
            sum_s+=diff
        return sum_s
