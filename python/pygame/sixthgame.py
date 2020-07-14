import pygame
import random

# bubble Sort

arr_cnt = 50
screen_width = arr_cnt * 4
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()
gb = [0, 0]
BLUE  = (  0,   0, 255)
BLACK = ( 0,0,0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

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
            pygame.draw.rect(screen, WHITE, pos, 2)

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
    stage = 0

    while run:
        # reset arr 
        if count == 0 or len(arr) - stage - 1 == 0 :
            arr = []
            for i in range(0, arr_cnt) :
                arr.append(random.randint(0, screen_height))
            selected = 0
            count = 0
            stage = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(pygame.color.Color(0, gb[0], gb[1]))
        arr = sortSelected(arr, selected)
        drawArr(arr, selected)
        pygame.display.flip()
        clock.tick(500)
        selected += 1
        selected %= len(arr) - stage - 1
        count += 1
        count %= (arr_cnt-1)*(arr_cnt-1 - stage)

        if selected == 0 :
            stage += 1

    pygame.quit()

if __name__ == '__main__' :
    pygame.init() 
    pygame.display.set_caption("Hello, pygame!")
    runGame()