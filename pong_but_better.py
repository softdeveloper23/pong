import pygame
import random

pygame.init()

gadget_pair = 1
ch = int(input("Enter your choice for the gadget pair: "))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong But Better")
run = True
direction = [0, 1]
angle = [0, 1, 2]

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
ball_vel_x, ball_vel_y = 0.2, 0.2
dummy_ball_x, dummy_ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.2, 0.2

# Paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = 100 - paddle_width / 2, WIDTH - (100 - paddle_width / 2)
right_paddle_vel = left_paddle_vel = 0

# Gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

# Main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget = 2
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # Ball movement control
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if dummy_ball_y <= 0 + radius or dummy_ball_y >= HEIGHT - radius:
        dummy_ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.5, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = -0.5, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.2, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = -0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.2, 0.5
                dummy_ball_vel_y, dummy_ball_vel_x = -0.2, 0.5
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.5, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = 0.5, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.2, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = 0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.2, 0.5
                dummy_ball_vel_y, dummy_ball_vel_x = 0.2, 0.5
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1

    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.5, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = -0.5, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.2, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = -0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.2, 0.5
                dummy_ball_vel_y, dummy_ball_vel_x = -0.2, 0.5
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.5, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = 0.5, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.2, 0.2
                dummy_ball_vel_y, dummy_ball_vel_x = 0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.2, 0.5
                dummy_ball_vel_y, dummy_ball_vel_x = 0.2, 0.5

    # Paddle movement control
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # Paddle collision
    # Left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            dummy_ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
            dummy_ball_vel_x *= -1
    # Right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            dummy_ball_x = right_paddle_x
            ball_vel_x *= -1
            dummy_ball_vel_x *= -1

    # Gadgets in action
    if gadget_pair == 1:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -3.5
                    left_gadget = 0
                    left_gadget_remaining -= 1
        elif left_gadget == 2:
            left_paddle_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    ball_vel_x *= -3.5
                    right_gadget = 0
                    right_gadget_remaining -= 1
        # Second pair
        elif right_gadget == 2:
            right_paddle_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1
        elif gadget_pair == 2:
            if left_gadget == 1:
                if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                    if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                        ball_x = left_paddle_x + paddle_width
                        dummy_ball_x = left_paddle_x + paddle_width
                        ball_vel_x *= -1
                        dummy_ball_vel_x *= -1
                        dummy_ball_vel_y *= -1
                        left_gadget = 0
                        left_gadget_remaining -= 1
            if right_gadget == 1:
                if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                    if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                        ball_x = right_paddle_x
                        dummy_ball_x = right_paddle_x
                        ball_vel_x *= -1
                        dummy_ball_vel_x *= -1
                        dummy_ball_vel_y *= -1
                        right_gadget = 0
                        right_gadget_remaining -= 1

    # Movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummy_ball_x += dummy_ball_vel_x
    dummy_ball_y += dummy_ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    # OBJECTS
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(
        wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    )
    pygame.draw.rect(
        wn,
        RED,
        pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height),
    )

    # Dummy ball section
    pygame.draw.circle(wn, BLUE, (dummy_ball_x, dummy_ball_y), radius)

    # Gadget activated indicator
    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

    pygame.display.update()
