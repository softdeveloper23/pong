import pygame

pygame.init()

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong But Better")

run = True

# Main loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
