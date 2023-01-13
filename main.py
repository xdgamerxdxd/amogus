import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('amogus.png')
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    # Moving player
    def moving(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN] and self.rect.bottom < 500:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    # making enemy
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('repor.png')
        self.surf = pygame.transform.scale(self.surf, (70, 70))
        self.surf.set_colorkey((255, 255, 255),pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(500 + 20, 500 + 100),
                random.randint(0, 500),
            )
        )
        self.speed = random.randint(1, 3)

    # enemy moving
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship,self).__init__()
        self.surf = pygame.image.load('spaship.png')
        self.surf = pygame.transform.scale(self.surf, (100,100))
        self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(500 + 20, 500 + 100),
                random.randint(0, 500),
            )
        )
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()

screen = pygame.display.set_mode([500, 500])

# Making evvent
addenemy = pygame.USEREVENT + 1
pygame.time.set_timer(addenemy, 500)

addspaship = pygame.USEREVENT + 2
pygame.time.set_timer(addspaship, 1000)

player = Player()


spaships = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()

running = True
while running == True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif keys[pygame.K_ESCAPE]:
            running = False

        elif event.type == addenemy:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == addspaship:
            new_spaship = Spaceship()
            spaships.add(new_spaship)
            all_sprites.add(new_spaship)

    enemies.update()
    spaships.update()
    player.moving(keys)

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False
        print('You got reported, sus')

    screen.blit(player.surf, player.rect)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
