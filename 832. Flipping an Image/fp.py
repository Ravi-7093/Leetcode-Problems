class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        new_lst=[]
        for i in image:
                lst=[]
                i.reverse()
                for j in i:
                    if(j==0):
                        j=1
                        lst.append(j)
                    else:
                        j=0
                        lst.append(j)
                new_lst.append(lst)
        return new_lst
