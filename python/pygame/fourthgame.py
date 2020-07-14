import pygame
import random

# 7개(runGame에서 생성된 Circle의 수)의 원이
# 처음에는 같은 타이밍에 생성되어서 커졌다가 작아지고
# 그다음에는 랜덤 타이밍과, 랜덤 포지션, 랜덤 컬러로 커졌다가 작아졌다를 반복한다.

screen_width = 400
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()
gb = [255, 255]
BLUE  = (  0,   0, 255)
run = True
status = 1 
position = [60, 100]
min_radius = 4
max_radius = 200

class Circle :
    def __init__(self) : 
        # 색 랜덤
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # 포지션 랜덤
        self.position = [random.randint(10, screen_width), random.randint(10, screen_height)]
        self.radius = min_radius
        self.status = 1
        self.isDrawable=True

    def getDrawable(self) : 
        return self.isDrawable

    def goNextSize(self) :
        if self.isDrawable :
            if self.status == 1 :
                if self.radius >= max_radius :
                    self.status = 0
                else :
                    self.radius += 4
            elif self.status == 0 :
                if self.radius <= 10 :
                    self.status = 1
                    self.position = [random.randint(0, 400), random.randint(0, 300)]
                    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    self.isDrawable = False
                else :
                    self.radius -= 4

    def drawCircle(self) :
        return  pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def CanIDraw(self) : 
        if random.randint(0, 30) == 15 :
            self.isDrawable = True

def runGame() :
    global run, gb, status, position
    # Game Loop
    circles = []
    for i in range(0, 7) :
        circles.append(Circle())

    while run:
        # 1) 사용자 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for circle in circles :
            if circle.getDrawable() :
                circle.goNextSize()
            else :
                circle.CanIDraw()

        # 3) 게임 장면 그리기
        screen.fill(pygame.color.Color(255, gb[0], gb[1]))
        for circle in circles :
            if circle.getDrawable() :
                circle.drawCircle()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__' :
    pygame.init() 
    pygame.display.set_caption("Hello, pygame!")
    # 1 is getting bigger
    # 0 is getting smaller
    runGame()