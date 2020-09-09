# 자물쇠 N * N 크기의 정사각 격자 형태
# 열쇠  M * M 크기의 정사각 격자 형태

# M <= N
# key, lock 0, 1 -> 0 홈, 1 돌기

# key를 회전, 오른쪽, 왼쪽 이동 하는 경우의 함수

def rotate() :
    pass

def move() :
    



if __name__ == '__main__' : 
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
