#Printing and looping

def print_even(n) : 
    print("Even numbers:")
    for i in range(0, n+1) :
        if i % 2 == 0 :
            print(i)

def print_odd(n) : 
    print("Odd numbers:")
    for i in range(0, n+1) :
        if i % 2 != 0 :
            print(i)

def read_positive() : 
    while True :
        temp = input("Please give a positive integer : ")
        if int(temp) > 0 : 
            print_even(int(temp))
            print_odd(int(temp))
            break
        else :
            continue

read_positive()


##TO DELETE :: input is float --> occur error