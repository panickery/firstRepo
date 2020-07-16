import pygame
import random

# 예전에 어디선가 본적있는 정렬의 효율을 알기위한 바그래프 정렬
# 한번 만들어 보고 싶었는데 능력 부족이었음
# 시도

arr_cnt = 50
screen_width = arr_cnt * 4
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()
gb = [255, 255]
BLUE  = (  0,   0, 255)
PURPLE = (255, 0, 255)
run = True

def sort(arr) : 
    for el in arr :
        for i in range(0, len(arr) - 1) :
            if arr[i] > arr[i + 1] :
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp

def drawArr(arr, selected) :
    for cnt in range(0, len(arr)) : 
        pos = [cnt*4, screen_height-arr[cnt], 2, arr[cnt]]
        if cnt == selected :
            pygame.draw.rect(screen, PURPLE, pos, 2)    
        else :
            pygame.draw.rect(screen, BLUE, pos, 2)

def sortSelected(arr, selected) :
    if arr[selected] > arr[selected + 1] :
        temp = arr[selected + 1]
        arr[selected + 1] = arr[selected]
        arr[selected] = temp
    return arr

def runGame() :
    global run, gb
    # Game Loop
    arr = []
    selected = 0
    count = 0

    while run:
        if count == 0 :
            arr = []
            for i in range(0, arr_cnt) :
                arr.append(random.randint(0, screen_height))
            selected = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(pygame.color.Color(255, gb[0], gb[1]))
        arr = sortSelected(arr, selected)
        drawArr(arr, selected)
        pygame.display.flip()
        clock.tick(500)
        selected += 1
        selected %= len(arr) - 1
        count += 1
        count %= (arr_cnt-1)*(arr_cnt-1)
    pygame.quit()

if __name__ == '__main__' :
    pygame.init() 
    pygame.display.set_caption("Hello, pygame!")
    runGame()