import random

def makeParen(num) :
    # 20
    test = list('()'*num)
    random.shuffle(test)

    return test



if __name__ == '__main__' :
    result_list = makeParen(100)

    print(''.join(result_list))