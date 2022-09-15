class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize=maxSize#initaliz the max size
        self.lst=[]#create an emoty lsit

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if(len(self.lst)<self.maxSize):# check if the length of the stack is less than the max_size 
            self.lst.append(x)#if true append to stack
        
        
            

    def pop(self):
        """
        :rtype: int
        """
        if(len(self.lst)<1):#check if the stack is empty 
            return -1
        else:
            return self.lst.pop(-1)# else return the top of the element
    
    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if(len(self.lst)<k):#validate if length of the array is less than k
            for i in range(len(self.lst)):
                self.lst[i]=self.lst[i]+val#add all the element with given val
        else:
            for i in range(k):#else add val only the elements which are less than k ie leaving the top element of the stack
                self.lst[i]=self.lst[i]+val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
