class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new_arr = nums.copy()
        new_arr.sort()
        res=[]
        d={}
        res  = [None] * k
        for i in range(len(new_arr)-k,len(new_arr)):
            d[new_arr[i]]=d.get(new_arr[i],0)+1
        j=0
        for n in nums:
            if(j<k and n in d):
                    res[j]=n
                    if(d[n]==1):
                        d.pop(n)
                    elif d[n] > 1:              
                        d[n] -= 1
                    j += 1
        return res      
