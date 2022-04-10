  def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0 # intialize the result to zero 
        l,r = 0, len(height)-1 # Using 2 pointer approach (l -->be left pointer and r-->be the right pointer )
        
        while(l<r): #left pointer<right pointer
            area = min(height[l],height[r]) * (r-l) #logic ---> get the min height b/w the columns and calculate the distance b/w them
            res = max(area,res) #get max area
            if height[l]<height[r]: # move left pointer forward if height of left column is less than right column
                l+=1
            else:
                r-=1
        return res
