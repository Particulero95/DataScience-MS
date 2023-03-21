import pygame
import sys

# initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pac-Man")

# load images
pacman_image = pygame.image.load("pacman.png").convert()
pacman_rect = pacman_image.get_rect()

# set up game variables
pacman_speed = 5
pacman_direction = "right"

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # move pacman
    if pacman_direction == "right":
        pacman_rect.move_ip(pacman_speed, 0)
        if pacman_rect.right >= screen.get_width():
            pacman_direction = "left"
    elif pacman_direction == "left":
        pacman_rect.move_ip(-pacman_speed, 0)
        if pacman_rect.left <= 0:
            pacman_direction = "right"
    
    # draw the screen
    screen.fill((0, 0, 0))
    screen.blit(pacman_image, pacman_rect)
    pygame.display.flip()


##fail
