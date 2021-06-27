nums=[6,-1,-3,4,-2,2,4,6,-12,-7]
f={0:1}
sum=0
k=0
ans=0
for i in range(len(nums)):
    
    sum+=nums[i]
    
    if sum-k in f:
        
        ans+=f[sum-k]]

    if sum not in f:
        
        f[sum]=1
    else:
        f[sum]+=1

print(ans)
    
