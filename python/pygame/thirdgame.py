import pygame
import random

pygame.init() 
screen = pygame.display.set_mode((400, 300)) 
pygame.display.set_caption("Hello, pygame!")

clock = pygame.time.Clock()
run = True
gb = [255, 255]

BLUE  = (  0,   0, 255)
radius = 400
# 1 is getting bigger
# 0 is getting smaller
status = 1 
position = [60, 100]

# Game Loop
while run:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 2) 게임 논리 실행
    # if gb[0] == 0:
    #     gb[0] = 255
    #     gb[1] = 255
    # else:
    #     gb[0] -= 1
    #     gb[1] -= 1

    if status == 1 :
        if radius >= 400 :
            status = 0
        else :
            radius += 4
    elif status == 0 :
        if radius <= 10 :
            status = 1
            position = [random.randint(0, 400), random.randint(0, 300)]
            print(position)
        else :
            radius -= 4

    # print(radius)
    # 400radius small
   
    # 3) 게임 장면 그리기
    screen.fill(pygame.color.Color(255, gb[0], gb[1]))
    pygame.draw.circle(screen, BLUE, position, radius, 2)
    # pygame.draw.circle(screen, BLUE, [position[0], position[1] - 100], radius, 2)
    pygame.display.flip()
    
    clock.tick(120)

pygame.quit()