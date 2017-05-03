import pygame, sys

pygame.init()

pygame.mixer.init() # initialize sound mixer

windowSize = (800,600)
screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("PS circle.png") # now rendering image

helloWorldSize = helloWorld.get_size() # getting size of helloworld string

sound = pygame.mixer.Sound("Pluralsight.wav")

pygame.mouse.set_visible(0) # this hides mouse cursor

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
        sound.stop() # to ensure that sound is not playing
        sound.play()
        
    if y + helloWorldSize[1] > 600: # fix for bottom
        y= 600 - helloWorldSize[1] 
        sound.stop()
        sound.play()
    if x == 0 or y==0:
        sound.stop()
        sound.play()        
        
    
    screen.blit(helloWorld,(x,y))  
    
    pygame.display.update()
