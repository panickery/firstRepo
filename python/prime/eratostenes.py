# prime 100000 -> 5.35401463508606
# prime 10000 -> 0.512005
# prime 1000 -> 0.3580805762100

# 특이하게 n의 범위에 따라 시간이 변함.
# 공간이 많이 필요해서 메모리 에러가 날수 있긴 함

import time
start = time.time()
pri_list = []

n=10000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    if len(primes) == 100000 :
        break

print(len(primes))
print("time :: ", time.time() - start)  
# print(a)