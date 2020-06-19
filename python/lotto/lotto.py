import argparse
import random
import sys

## Lotto 확률 분석 및 테스트
#생각해보니 1등과 2등은 보너스 번호가 있는데 안넣었다.
#빠가사리! 수정 필요

def get_number() :
    answer = set()
    while len(answer) != 7 :
        answer.add(random.randint(1, 45))
    return answer

def get_lotto(count) : 
    lotto_bill = []
    for cnt in range(count) :
        lotto_bill.append(get_number())
    return lotto_bill

def compare_lotto(answer, lotto) : 
    results = []
    for lot in lotto : 
        result = answer & lot
        results.append(result)
    return results

if __name__ == '__main__' : 
    # give argument count as bought lotto
    parser = argparse.ArgumentParser(description='Predict your prize.')
    parser.add_argument('count', help="How many you buy lotto")
    args = parser.parse_args()

    if args.count == None : 
        print('No Argument!')
        sys.exit(0)

    answer = get_number()
    lotto_bill = get_lotto(int(args.count))
    print('you buy {}bill'.format(int(args.count)))
    print('you spend {}won'.format(int(args.count) * 1000))

    results = compare_lotto(answer, lotto_bill)

    scores = []
    sum = 0
    for i in results : 
        score = len(i)
        scores.append(score)
        if score == 3 : 
            sum += 5000
        elif score == 4 :
            sum += 50000
        elif score == 5 :
            sum += 1200000
        elif score == 6 :
            sum += 1000000000
    
    result_money = sum - (int(args.count) * 1000)
    
    print("you earned {}won".format(result_money))
    
    for cnt in range(0, 7) :
        print("{} correct :: {}".format(cnt, scores.count(cnt))) 
