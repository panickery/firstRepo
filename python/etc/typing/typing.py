import os
import sys
import time


def searchFile(f_nm, c_path) :
    temp_list = os.listdir(c_path)

    for i in temp_list :
        temp_path = os.path.join(c_path, i)
        search_path = None

        if os.path.isdir(temp_path) :
            search_path = searchFile(f_nm, temp_path)
            if search_path :
                return search_path
        elif os.path.isfile(temp_path) :
            if "메밀" in temp_path :
                return temp_path
    return None

if __name__ == '__main__' :
    
    # file_list = []
    file_nm = "메밀꽃"
    cur_path = os.path.join(os.getcwd(), "firstRepo")
    # cur_path = os.getcwd()
    print("Current dir :: ", cur_path)
    print("Start searching File")
    start = time.time()
    search_file_nm = searchFile(file_nm, cur_path)
    end = time.time()

    print("Spend Time :: {}".format(end-start))

    if search_file_nm == None:
        print("File Not Found")
        sys.exit()
    else :
        pass

    f = open(search_file_nm, 'r', encoding='utf-8')
    input("엔터 후 시작 -")

    start = time.time()
    len_char = 0
    len_right = 0

    while True :
        line = f.readline()
        print(line, end='')
        inp_str = input()

        if "quit" in inp_str :
            end = time.time()
            print("걸린시간 : {}초".format(end-start))
            print("총글자 / 맞춘글자 :: {} / {}".format(len_char, len_right))
            print("정확도 :: {}%".format((len_right/len_char) * 100))
            sys.exit()
        else :
            len_char += len(line)

            # 맨뒤에 줄바꿈이 붙어있음
            for i in range(len(line)-1) :
                if line[i] == inp_str[i] :
                    len_right+=1




