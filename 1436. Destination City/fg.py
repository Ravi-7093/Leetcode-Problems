d={}
for i in paths:
   d[i[0]]=i[1]
for i in d.values():
   des=d.get(i)
if not des:
   return i
