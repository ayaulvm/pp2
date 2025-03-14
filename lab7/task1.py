import pygame
import os
import time
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()


background = pygame.image.load("mickeyclock.jpg")  
minute_hand = pygame.image.load("min.png")  
second_hand = pygame.image.load("sec.png")  

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (150, 20))
second_hand = pygame.transform.scale(second_hand, (150, 20))

def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    
    minute_angle = (minutes % 60) * 6  
    second_angle = (seconds % 60) * 6  
    
    
    clock_center = (WIDTH // 2, HEIGHT // 2)
    
    
    rotated_minute, min_rect = rotate_hand(minute_hand, minute_angle, clock_center)
    rotated_second, sec_rect = rotate_hand(second_hand, second_angle, clock_center)
    
    
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
