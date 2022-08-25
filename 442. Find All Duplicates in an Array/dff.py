def findDuplicates():
    nums = [4,3,2,7,8,2,3,1]#
    d={}# create an empty dictionary 
    ans=[]#create an empty list 
    for i in range(len(nums)):#traverse the array
        d[nums[i]]=d.get(nums[i],0)+1#store the occurences of each letter 
    for key,value in d.items():#iterate the values in the dictionary 
        if(value>1):#if value greater than 1
            ans.append(key)#append the value to the key
    ans.sort()#sort the list in descending order 
    return ans#return the list 
        
print(findDuplicates())
