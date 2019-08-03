num=list(map(int,input().split()))[:n]
count=0
for x in range (0,n):
  if k==num[x]:
    count+=1
print(count)  
