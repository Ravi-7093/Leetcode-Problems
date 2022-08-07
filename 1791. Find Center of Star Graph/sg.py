class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        lst=[]#create an empty list 
        lst.append(edges[0][0])#append first element
        lst.append(edges[0][1])#append second element 
        count=0 #edge count 
        new_count=0 # track count for first node
        new_count_two=0 #track count for second node 
        for i in edges:#get the count of total edges
            count+=1
        for i in edges:# check if first node is present in all edges 
            if lst[0] in i:
                new_count+=1
        for i in edges:
            if lst[1] in i:# check if second node is present in all edges 
                new_count_two+=1
        if(new_count==count): #if count of the nodes is equal to no of edges then we found the edge 
            return lst[0]
        else:
            return lst[1]
