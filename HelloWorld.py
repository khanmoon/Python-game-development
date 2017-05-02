import pygame, sys

pygame.init()

windowSize = (800,600 )
screen = pygame.display.set_mode(windowSize)
myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello World", 1, (255,0 ,255),(255,255,255))

helloWorldSize = helloWorld.get_size() # getting size of helloworld string

x,y = 0,0 # to use the position of helloworld string

directionX = 1
clock = pygame.time.Clock()

while 1:
    
    clock.tick(40) # it ensures us that the python will render 40 fps
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill((0,0,0)) # it blacks the screen on start of every loop
    screen.blit(helloWorld,(x,y))
    
    x+=5 * directionX
    
    if x+ helloWorldSize[0] > 800 or x<=0: # this improves the left motion
        directionX*=-1
    
    pygame.display.update()
