class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_height=0
        height=0
        for i in range(len(gain)):
            height+=gain[i]
            max_height=max(max_height, height)
        return max_height
        
