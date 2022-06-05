class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if(len(s)!=len(goal)): #check for different length
            return False
        
        if(s==goal and len(set(s))<len(s)): # if strings are same but does not contain unique characters 
            return True
        
        diff=[]
        for i in range(len(s)):
            if(s[i]!=goal[i]): # check for the different strings within the list
                diff.append([s[i],goal[i]]) # append it as list of lists
                
        if(len(diff)==2 and diff[0]==diff[-1][::-1]):#only if len is greater than 2 and the list index one and two(value is reversed) are compared  
            return True
        return False
                    
