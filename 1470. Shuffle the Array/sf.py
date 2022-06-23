lst=[]
for i in range(n):
  print(nums[i])
  lst.append(nums[i])
  lst.append(nums[n+i])
return lst
