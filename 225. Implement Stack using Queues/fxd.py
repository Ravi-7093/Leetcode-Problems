class MyStack(object):

    def __init__(self):
        self.lst=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lst.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if(len(self.lst)<1):
            return None
        else:
            return self.lst.pop(len(self.lst)-1)

    def top(self):
        """
        :rtype: int
        """
        return self.lst[len(self.lst)-1]

    def empty(self):
        """
        :rtype: bool
        """
        if (len(self.lst)<1):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
