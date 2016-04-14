import pygame
        
width = 800
height = 600

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('UnQualcosa!')
clock = pygame.time.Clock()

BLAK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


done = False
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.draw.circle(screen, BLUE,[400,300], 20)
        while 1:
            pygame.draw.circle(screen, BLUE,[randomi,random], 10)
    
        
        
        
        pygame.display.update()
        clock.tick(60)
finally:
    pygame.quit()
