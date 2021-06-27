import math
n=9
c=0
sq=math.floor(math.sqrt(9))
for i in range(1,sq+1):
    if math.pow(i,2)<n:
        c+=1
        
print(c)
