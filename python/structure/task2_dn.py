#Distinct numbers

def distinct(lst) :
    if len(lst) == len(set(lst)) :
        return True
    return False

print(distinct([3, 4, 6, 2, 7, 9]))
print(distinct([3, 4, 6, 2, 7, 9, 2]))