import pygame, sys

pygame.init()

windowSize = (800,600)
screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("PS circle.png") # now rendering image

helloWorldSize = helloWorld.get_size() # getting size of helloworld string

x,y = 0,0 # to use the position of helloworld string

directionX,directionY = 1, 1
clock = pygame.time.Clock()

while 1:
    
    clock.tick(40) # it ensures us that the python will render 40 fps
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill((0,0,0)) # it blacks the screen on start of every loop
     
    
    mouseposition = pygame.mouse.get_pos()
    x,y = mouseposition
    
    if x+helloWorldSize[0]>800: #fix right side
        x = 800 - helloWorldSize[0]
        
    if y + helloWorldSize[1] > 600: # fix for bottom
        y= 600 - helloWorldSize[1] 
    
    screen.blit(helloWorld,(x,y))  
    
    pygame.display.update()
