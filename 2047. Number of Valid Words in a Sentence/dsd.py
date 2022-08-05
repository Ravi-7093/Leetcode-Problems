def countValidWords():
        """
        :type sentence: str
        :rtype: int
        """
        sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
        words = [word.strip() for word in sentence.split(" ") if word !=""] #strip the string 
        count = 0
        for word in words:
            valid,containHyphen = True,False #check for validation of each word
            for i in range(len(word)):
                if (not(word[i].islower() or word[i]=='-' or word[i]=='!'or word[i]=='.' or word[i]==',' )): #check if each character is according to the requirement
                    valid = False
                    break
                if(word[i] =='-'):
                    if(not(0<i<len(word)-1 and word[i-1].islower() and word[i+1].islower() and not containHyphen)):#check for '-'
                        valid = False
                        break
                    containHyphen = True
                if(word[i] =='!' and i!= len(word)-1):
                    valid = False
                    break
                if((word[i] ==',' or word[i] =='.') and (i!= len(word)-1)):
                    valid = False
                    break
            if(valid):        
                count += 1
        return count
print(countValidWords())
