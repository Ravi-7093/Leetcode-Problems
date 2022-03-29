class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        P,Q = len(num1),len(num2)#Computing length of the strings
        i,j=P-1,Q-1 # Initalizing the values for i and j to traverse the strrings from the end
        output="" #Used to store the output after adding two strings
        carry=0   #Used to store the carry value after adding
        while(i>=0 or j>=0):
            a,b=0,0 #storing the numerical value of the character
            if(i>=0):
                a=ord(num1[i])-48 #Computing the numerical value for each character using ordinal function
                i-=1
            if(j>=0):
                b=ord(num2[j])-48
                j-=1
            temp=a+b+carry #Used to store the result of sum of two characters of the strings 
            if(temp>9): # If temp is greater than 9 we get a carry and carry is set to 1.
                carry=1
            else:
                carry=0
            output=str(temp)[-1]+output #Storing the value of the output from temp from the end 
           
        if carry:
                output="1"+output #After computing if there is a carry append it to begining
        return output
