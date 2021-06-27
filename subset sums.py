from itertools import combinations


def findcomb(key,l):
        return list(combinations(l,key))
    

def check(lis,a,b):
    count=0
    for i in lis:
        if sum(i)>=a and sum(i)<=b:
            count+=1

    return count


for _ in range(int(input())):
    N,a,b=map(int,input().split())
    l=[]
    for i in range(N):
        l.append(int(input()))
    key=1
    c=0
    while key<=N:
       lis= findcomb(key,l)
       c+=check(lis,a,b)
       key+=1
    print(c+1)
    
