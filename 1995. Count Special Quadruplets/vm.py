def countGoodTriplets():
    nums = [1,2,3,6]
    print(nums)
    count=0
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for p in range(k+1,len(nums)):
                   print(nums[i],nums[j],nums[k],nums[p])
                   if(nums[i] + nums[j] + nums[k] == nums[p]):
                       count=count+1
    return count
