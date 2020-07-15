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
BLUE  = (  0,   0, 255)
BLACK = ( 0,0,0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)
font = None
run = True

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

# def sortSelected(arr, selected) :
#     if arr[selected] > arr[selected + 1] :
#         temp = arr[selected + 1]
#         arr[selected + 1] = arr[selected]
#         arr[selected] = temp
#     return arr

def sortSelected(arr, i, j, least) :

    return arr, i, j, least

def basicScreen() : 
    screen.fill(pygame.color.Color(0, gb[0], gb[1]))
    # text = font.render(str(count), True, WHITE)
    # screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(500)

def runGame() :
    global run, gb
    # Game Loop
    arr = []
    selected = 0
    count = 0
    stage = 0

    arr.append(random.randint(0, screen_height))

    while run:
        print("good2")
        
        for i in range(0, len(arr)-1) :
            print(i)
            least = i
            for j in range(i+1, len(arr)) :
                if arr[least] > arr[j] :
                    least = j
                drawArr(arr, j)
                basicScreen()
                print("good")

            if i != least :
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

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