a=[0,0,2,1,1]
l=[0]*4

list1=[]
N=3
n=5
for i in range(n):
    for  j in range(i+1,n):
        for k in range(j+1,n):
            su=a[i]+a[j]+a[k]
            
            find=N-su
  
            if find in a[k+1:n]:
                l[0],l[1],l[2],l[3]=a[i],a[j],a[k],find
                l.sort()
                l.append('$')
                list1.append(l)
                l=[0]*4
print(list1)
            
                

      
