# prime 100000 -> 9.429881
# prime 10000 -> 0.3789925
# prime 1000 -> 0.020000

import math
import time
start = time.time()
pri_list = []

if __name__ == '__main__' :
    
    for i in range(0, 10000000) :
        if i == 0 or i == 1 :
            continue
        elif i == 2 :
            pri_list.append(i)
        else :
            bool_div = True
            for pri in pri_list :
                if pri > math.sqrt(i) : 
                    break
                if i % pri == 0 :
                    bool_div = False
                    break
                else :
                    continue
            if bool_div :
                pri_list.append(i) 

        if len(pri_list) == 10000 :
            break;
    
    print(len(pri_list))
    print("time :: ", time.time() - start)  
