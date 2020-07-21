import pygame
import random
import time
import copy

# quick sort

arr_cnt = 50
screen_width = arr_cnt * 4
screen_height = 300
arr_stage = []

screen = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()
gb = [0, 0]
BLUE  =  (  0,   0, 255)
BLACK  = (  0,   0,   0)
PURPLE = (255,   0, 255)
WHITE  = (255, 255, 255)
font = None
run = True

def partition(arr, l, h): 
    global arr_stage
    temp_arr = [copy.deepcopy(arr), 0]
    arr_stage.append(temp_arr)
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l, h): 
        temp_arr = [copy.deepcopy(arr), x]
        arr_stage.append(temp_arr)
        if arr[j] <= x: 
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    temp_arr = [copy.deepcopy(arr), x]
    arr_stage.append(temp_arr)
    return (i + 1) 
  
# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l  --> Starting index, 
# h  --> Ending index 
def quickSortIterative(arr, l, h): 
    global arr_stage
    temp_arr = [copy.deepcopy(arr), 0]
    arr_stage.append(temp_arr)
  
    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    # Keep popping from stack while is not empty 
    while top >= 0: 
        temp_arr = [copy.deepcopy(arr), 0]
        arr_stage.append(temp_arr)
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h ) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

        temp_arr = [copy.deepcopy(arr), p]
        arr_stage.append(temp_arr)

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
    global run, gb, arr_stage
    # Game Loop
    arr = []
    count = 0
    notEnd = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not notEnd :
            arr_stage = []
            arr = resetArray()
            start = time.time()
            quickSortIterative(arr, 0, len(arr)-1) 
            end = time.time()
            print("sorting time :: {}".format(end-start))
            print(len(arr_stage))
            count = 0

        screen.fill(pygame.color.Color(0, gb[0], gb[1]))
        drawArr(arr_stage[count][0], arr_stage[count][1])
        if count == len(arr_stage) - 1 :
            notEnd = False
            pygame.time.wait(1000)
        else :
            notEnd = True
        basicScreen(count)
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