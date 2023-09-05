import pygame

pygame.init()

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong But Better")

run = True

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius

# Paddles
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = 100 - paddle_width / 2, WIDTH - (100 - paddle_width / 2)

# Main loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(
        wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    )
    pygame.draw.rect(
        wn,
        RED,
        pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height),
    )
    pygame.display.update()
