a=[-30, 8, 23 ,6 ,10, 9, 31, 7, 19, 20, 1, 33, 21, 27, 28, 3, 25, 26]
n=len(a)
print(n)
c=0
x=86
a.sort()                            
for i in range(n-2):
    l=i+1
    r=n-1
    while(l<n):
        
        if l<r:
            su=a[i]+a[l]+a[r]
            if su <x:
                print(a[i],a[l],a[r])
                c+=1
                r-=1
            else:
                
                r-=1
        else:
            l+=1
            r=n-1
        
print(c)
