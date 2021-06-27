import math
from re import findall

def end_zeros(num):
    return len(findall("0*$", str(num))[0])
def istrail(n,mid):
    f=math.factorial(mid)
  
    count=end_zeros(f)
    if count==n:
        return True
    else:
        return False
            


for _ in range(int(input())):
        n=84
        low=0
        high=5*n
        res=0
        while(low<=high):
            mid=(low+high)//2
            if (istrail(n,mid)):
                high=mid-1
                res=mid
                
            else:
                low=mid+1
        print(res)
