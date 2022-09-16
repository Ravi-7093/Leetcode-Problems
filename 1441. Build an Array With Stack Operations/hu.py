class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack=[]#create an empty stack
        lst=[]#create an emopty  list 
        for i in range(1,n+1):#iterate the values in the range 
            stack.append(i)#append the value to the stack
            lst.append("Push")#append the operation name performed to the list
            if i not in target:#chekc if the element pushed into stack from range is present in target 
                stack.pop(-1)#else pop from stack 
                lst.append("Pop")#and append the  operation performed to the list 
            else:
                count=0#create  counter 
                if len(stack)==len(target):#check for if the lengths of stack abd target are same 
                    print("Hi",len(stack))
                    for i in range(len(stack)):#check if all the elements in the stack and target are equal 
                        if stack[i]==target[i]:
                            count+=1
                    if count==len(target):#if true exit from the loop
                        break
        return lst
