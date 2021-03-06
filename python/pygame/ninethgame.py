import pygame
import random
import time

# counting sort

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

arr_stage = []

def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1
 
    ndx = 0
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1

# 한번 부를때마다 다음 단계를 return 해야한다.
def sortSelected(arr, i, arrMax, listing, ndx, counter) :
    if i < len(arr) and listing == 0 :
        counter[arr[i]] += 1
        i += 1
        return True, arr, i, arrMax, listing, ndx, counter
    elif listing == 0 :
        i = 0
        listing = 1

    if listing == 1 and i > arrMax : 
        pygame.time.wait(1000)
        return False, arr, i, arrMax, listing, ndx, counter

    if listing == 1 :
        if counter[i] > 0 : 
            arr[ndx] = i
            ndx += 1
            counter[i] -= 1
        else :
            i += 1
    
    return True, arr, i, arrMax, listing, ndx, counter

def drawArr(arr, selected) :
    for cnt in range(0, len(arr)) : 
        pos = [cnt*4, screen_height-arr[cnt], 2, arr[cnt]]
        if cnt == selected :
            pygame.draw.rect(screen, PURPLE, pos, 2)    
        else :
            pygame.draw.rect(screen, WHITE, pos, 2)

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
    i, j = 0, 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not notEnd :
            arr = resetArray()
            arrMax = max(arr)
            counter = [0] * (max(arr) + 1)
            i = 0
            j = 0
            listing = 0
            ndx = 0
            count = 0

        screen.fill(pygame.color.Color(0, gb[0], gb[1]))
        drawArr(arr, i)
        basicScreen(count)
        notEnd, arr, i, arrMax, listing, ndx, counter = sortSelected(arr, i, arrMax, listing, ndx, counter)
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