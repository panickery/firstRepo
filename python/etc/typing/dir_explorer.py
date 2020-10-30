#재귀적으로 directory를 탐험?
#실행하면 현재 디렉토리를 순회하며 하위 디렉토리의 폴더, 파일
# 을 모두 리스트에 넣는다.

import os
import time

def startExplore(d_list, f_list, c_path) :
    '''
    d_list :: directory list
    f_list :: file list
    c_path :: current path
    '''
    temp_list = os.listdir(c_path)
    # print(temp_list)

    for i in temp_list :
        # print(os.path.join(c_path, i))
        # time.sleep(1)
        # .git폴더에 굉장히 더러운게 많아서 숨김파일, 폴더는 무시하기로 하자
        if i[0] == '.' : 
            continue
        temp_path = os.path.join(c_path, i)

        if os.path.isdir(temp_path) :
            d_list.append(temp_path)
            startExplore(d_list, f_list, temp_path)
        elif os.path.isfile(temp_path) :
            f_list.append(temp_path)

# 어떻게 하면 재귀가 될까?
# 모든 파일들을 처음~ 끝경로까지 한 리스트에 넣는다면?


if __name__ =='__main__' :
    file_list = []
    dir_list = []
    # cur_path = os.getcwd()
    cur_path = os.path.join(os.getcwd(), "firstRepo")
    startExplore(dir_list, file_list, cur_path)

    # print(dir_list)
    # print(file_list)

    for i in file_list :
        if "메밀" in i :
            print(i)




