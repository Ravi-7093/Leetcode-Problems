class Logger(object):

    def __init__(self):
        self.d={}#create an empty dictionary 
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.d: # check if message in dictionary 
            timestamp=timestamp+10 # if its not there create an entry with timestamp
            self.d[message]=timestamp #
            return True# and return True
        else:
            if timestamp>=self.d[message]:# else if message present is there check if timestamp is greater than the present timestamp 
                timestamp=timestamp+10# if true update timestamp for the message 
                self.d[message]=timestamp
                return True#return true 
            else:
                return False#else return false


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
