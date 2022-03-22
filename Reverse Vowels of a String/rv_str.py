class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=0 # first pointer 
        y=len(s)-1 #second pointer 
        
        s=list(s) # Converting a string to list
        vow=["a","e","i","o","u","A","E","I","O","U"] #Create a list of vowels
        
        while(x<=y): 
            if(s[x] not in vow):#if the elemet in the string is not an consonant for the first pointer value 
                x+=1 #incremnt x
                continue# break the execution of the loop
            if(s[y] not in vow):# if the element in the string is not an consonant for the seond pointer va;ue
                y-=1 #decrement y
                continue #break the execution of the lopp
            s[x],s[y]=s[y],s[x] # swap the values of the elements in the string if they are vowels
            x+=1 #increment x for comparing the next character
            y-=1 
            
        return ''.join(s) #converting list to string using join method
