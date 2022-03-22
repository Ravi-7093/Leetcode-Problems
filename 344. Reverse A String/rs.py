class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j=len(s)-1 #second pointer 
        i=0 #first pointer 
        
        while(i<=j):
            temp=s[i] #move the first element to temp variable 
            s[i]=s[j] #move the last element to first position of the list
            s[j]=temp #move the temp value ie first list item to last index 
            i+=1 #increment first pointer
            j-=1 #decrement second pointer 
