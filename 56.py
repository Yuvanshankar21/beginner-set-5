a=(input())
l=len(a)
count=0
sum1=0
for x in range (l):
  if (a[x].isdigit()):
    count=count+1
  elif(a[x].isalpha()):
    sum1=sum1+1
if(count!=0 and sum1!=0):    
  print('Yes')
else:
  print('No')    
