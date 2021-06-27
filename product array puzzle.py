import math
nums=[10,3,5,6,2]
n=5
ltemp=[1]*n
rtemp=[1]*n
for i in range(1,n):
    ltemp[i-1]=math.prod(nums[i:])

for i in range(n-2,-1,-1):
    rtemp[i+1]=math.prod(nums[:i+1])
    
for i in range(n):
    ltemp[i]*=rtemp[i]
print(ltemp)
