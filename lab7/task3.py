import pygame

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
is_blue = True
x = 30
y = 30
radius = 25

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - radius*2 > 0 : y -= 20
        if pressed[pygame.K_DOWN] and y + radius*2 < screen_height: y += 20
        if pressed[pygame.K_LEFT] and x - radius*2 > 0: x -= 20
        if pressed[pygame.K_RIGHT] and x + radius*2 < screen_width: x += 20
        
        screen.fill((255, 255, 255))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.circle(screen, color, (x, y), radius)
        
        pygame.display.flip()
        clock.tick(60)