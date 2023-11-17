import pygame

pygame.init()
win = pygame.display.set_mode((700,700))

pygame.display.set_caption('game saya 1')


x = 330 
y = 320
width = 60
height = 60
vel = 5 

run = True
while run:
    pygame.time.delay(9) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_a]:
        x -= vel
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_d]:
        x += vel
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_w]:
        y -= vel
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_s]:
        y += vel
    win.fill((255,255,255))
    pygame.draw.rect(win, (125,30,255),(x, y, width, height))   
    pygame.display.update()