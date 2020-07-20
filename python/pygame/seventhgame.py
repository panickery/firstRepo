import pygame
import random
import time

# Selection sort

arr_cnt = 50
screen_width = arr_cnt * 4
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()
gb = [0, 0]
BLUE  =  (  0,   0, 255)
BLACK  = (  0,   0,   0)
PURPLE = (255,   0, 255)
WHITE  = (255, 255, 255)
font = None
run = True

# Selection Sort
def sort(arr) : 
    for i in range(0, len(arr)-1) :
        least = i
        for j in range(i+1, len(arr)) :
            if arr[least] > arr[j] :
                least = j
        if i != least :
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

def drawArr(arr, selected) :
    for cnt in range(0, len(arr)) : 
        pos = [cnt*4, screen_height-arr[cnt], 2, arr[cnt]]
        if cnt == selected :
            pygame.draw.rect(screen, PURPLE, pos, 2)    
        else :
            pygame.draw.rect(screen, WHITE, pos, 2)

# 한번 부를때마다 다음 단계를 return 해야한다.
def sortSelected(arr, i, j, least) :
    if j == len(arr) :
        if i != least :
            temp = arr[i]
            arr[i] = arr[least]
            arr[least] = temp
        i += 1
        j = i
        least = i
        # i is in End. it has to be reset
        if i == len(arr) : 
            pygame.time.wait(1000)
            return False, arr, i, j, least
        return True, arr, i, j, least

    if arr[least] > arr[j] :
        least = j

    return True, arr, i, j+1, least

def basicScreen(count) : 
    text = font.render(str(count), True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(500)

def resetArray() :
    arr = []
    for i in range(0, arr_cnt) :
        arr.append(random.randint(0, screen_height))
    return arr

def runGame() :
    global run, gb
    # Game Loop
    arr = []
    selected = 0
    count = 0
    notEnd = False
    # Selection Sort에서 i, j, least에 해당하는 부분 그대로 사용
    i, j, least = 0, 0, 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not notEnd :
            arr = resetArray()
            i = 0
            j = i+1
            least = i
            count = 0

        screen.fill(pygame.color.Color(0, gb[0], gb[1]))
        drawArr(arr, j)
        basicScreen(count)

        notEnd, arr, i, j, least = sortSelected(arr, i, j, least)
        count+=1

    pygame.quit()

if __name__ == '__main__' :
    pygame.init() 
    pygame.display.set_caption("Hello, pygame!")

    sysfont = pygame.font.get_default_font()
    print('system font :', sysfont)

    t0 = time.time()
    font = pygame.font.SysFont(None, 48)
    print('time needed for Font creation :', time.time()-t0)
    runGame()