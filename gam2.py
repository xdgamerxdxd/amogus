import time

import pygame

# object coordinates:
x = 250
y = 480

# object dimensions
swidth = 20
sheight = 20

    # object jump state
#Is object falling
T = False
# I object not falling
F = True
#timee in air
at = 1

vel = 10

screen = pygame.display.set_mode([500,500])

clock = pygame.time.Clock()

running = True
while running ==  True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif keys[pygame.K_ESCAPE]:
            running  = False

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - swidth:
        x += vel
    if keys[pygame.K_UP] and T == False:
        F = False
    if y <= sheight + 300:
        T = True
        F = True
    # Make thing go down
    if T == True and y  < 500 - sheight * 1.5:
        y += 10
    else:
        T = False
        at = 1

    # Make thing go up
    if F == False and y > sheight + 250 and at == 1:
        y -= 8.5
        if y > sheight + 250 and at == 1:
            at +=1
    elif  F == False and y > sheight + 300 and at == 2:
        y -= 2


    screen.fill((0,0,0))

    player = pygame.draw.rect(screen, (255,50,0), (x, y, swidth, sheight))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()