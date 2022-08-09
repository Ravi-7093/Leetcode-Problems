class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        d={} #empty dictionary
        for i in range(len(items1)): # iterate the items
            if(items1[i][0] in d ): #iterate over the dictionary if the value exists add the weight
                d[items1[i][0]]+=items1[i][1]
            else:
                d[items1[i][0]]=items1[i][1]#if the value is not present in dictionary , create a key value pair
        for i in range(len(items2)):
            if( items2[i][0] in d ):
                d[items2[i][0]]+=items2[i][1]
            else:
                d[items2[i][0]]=items2[i][1]
        ans=[]
        for i in sorted(d): #sort the dictionary
            ans.append([i, d[i]])#append the value and list as single list forming list of lists
        return ans  
