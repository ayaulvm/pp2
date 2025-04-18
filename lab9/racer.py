# Imports
import pygame, sys
from pygame.locals import * #основные клавиши для упрощения
import random, time

# Initialzing
pygame.init()

# FPS
FPS =60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0


# Setting up Fonts
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect() #получаем прямоугольник
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #по ширине случайно от 40 до 360, по высоте в самом верху экрана

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) #изменение координаты вниз
        if (self.rect.top > 600): #верхняя граница врага вышла за нижнюю границу экрана
            SCORE += 1
            self.rect.top = 0 #перерождается
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#added class Coin for coin to appear and to count the number of coins
c1,c2,c3,c4,c5 = False, False, False, False, False
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.svg")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        self.value = random.choice([1, 2, 3])

    def move(self):
        global COINS
        global SPEED
        COINS+=self.value
        global c1,c2,c3,c4,c5
        if not c1 and COINS>=10: #увеличение скорости зависит от колва собранных монет 
            SPEED+=1
            c1=True
        if not c2 and COINS>=20:
            SPEED+=1
            c2=True
        if not c3 and COINS>=30:
            SPEED+=1
            c3=True
        if not c4 and COINS>=40:
            SPEED+=1
            c4=True
        if not c5 and COINS>=50:
            SPEED+=1
            c5=True
        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        self.value = random.choice([1, 2, 3])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed() #список состояний всех клавиш клавиатуры
        if self.rect.left > 0: #проверяет не уехала ли за левый экран
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH: #не уехала ли за правую границу
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0: #не уехала ли вверх
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT: #не уехала ли вниз
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                
# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group() #класс позволяет объединить спрайты в коллекции
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event если пользователь ничего не делает
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000) #раз в секунду будет генерироваться инкспиид


def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: #нажата ли любая клавиша
                if event.key == K_SPACE:  # Продолжить игру при нажатии на пробел
                    return True
                elif event.key == K_ESCAPE:  # Закончить игру при нажатии на ESC
                    return False

def handle_crash():
    time.sleep(2) #игра замирает на две сек

background_y = 0  # фон начинается сверху

while True:
    for event in pygame.event.get(): #перебирает все события которые произошли внутри окна пайгейм
        if event.type == INC_SPEED:
            SPEED += 0.1 #увеличение скорости
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # If there is a collision between a player and an enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = handle_crash()
        if not continue_game:
            pygame.quit()
            sys.exit()
        game_over_screen()
        

    # Scroll the background
    background_y = (background_y + SPEED) % background.get_height() #mod для иллюзии бесконечности

    # Draw the background at the calculated position
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        # Increase the number of coins if collision with player happened
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # Move the second random car
    for enemy in enemies:
        enemy.move()

    # Move the coins
    for coin in coinss:
        coin.rect.y += SPEED

        # Respawn coins if they go off-screen
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height #монета за кадром медленно спускается
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    pygame.display.update()
    FramePerSec.tick(FPS)