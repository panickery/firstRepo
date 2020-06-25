# prime 10000 -> INF
# prime 1000 -> 2.6340

import time
start = time.time()

def isNumberPrime(number) :
    if number == 0 or number == 1 :
        return False
    else :
        div_cnt = 0
        for i in range(2, number) :
            if number % i == 0 :
                div_cnt += 1
        
        if div_cnt == 0 :
            return True
        else :
            return False

if __name__ == '__main__' :

    prime_cnt = 0
    i = 0
    while(True) :
        if isNumberPrime(i) :
            prime_cnt+=1

            if prime_cnt == 10000 :
                break
        i += 1
    
    print("time :: ", time.time() - start)


