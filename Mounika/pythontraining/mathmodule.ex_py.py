
#n = 2
#x = 2
#print(n*(n-1)*(math.pow(x,5)))/(math.factorial(5))
import math
for n in range(1,10):
    print("N = ",n,",sin" ,n, ":",round(math.sin(n),2),"log",n,":",round(math.log(n),2))
