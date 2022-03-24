class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[] #Create a empty list for the result
        for word in words:
            str="" #create an empty string
            for i in word: # for each char in the word get the arr (morse_value)
                str+=arr[ord(i)-97] # use the ascii value to get the index for the given array(morse) and append it empty string to create morse code for the given word
            if str not in res: # if the str(morse) not present in final result 
                res.append(str)# then append to resulting list
        return len(res) #return length
            
