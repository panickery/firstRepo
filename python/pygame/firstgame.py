import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pad_width = 1024
pad_height = 512

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image.fill(BLACK)

def runGame() :
    global screen, clock
    crashed = False
    count = 0
    while not crashed :
        if count % 300 == 0 :
            print(count)            
        count+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_w :
                    rect.move_ip(0, -2)
                elif event.key == pygame.K_s :
                    rect.move_ip(0, 2)
                elif event.key == pygame.K_a :
                    rect.move_ip(-2, 0)
                elif event.key == pygame.K_d :
                    rect.move_ip(2, 0)

        screen.fill(WHITE)
        screen.blit(image, rect)
        pygame.display.update()
        # 60 per second
        clock.tick(60)

    # Calling 'pygame.quit()' won't close the program! It will just uninitialize the modules.
    pygame.quit()


def initGame() :
    global screen, clock

    # success/failure test 
    # all module failed --> py.games fails
    successes, failures = pygame.init()
    print("{} successes and {} failures".format(successes, failures))
    # 
    screen = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('gameCaption')

    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__' :
    initGame()
