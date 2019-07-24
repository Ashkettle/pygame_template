import pygame
import settings




# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

x = 50
y = 50
width = 40
height = 60
velocity = 5


def set_player_movement():
    pass


# Game Loop
running = True
while running:
    pygame.time.delay(30)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    set_player_movement()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < settings.WIDTH - width - velocity:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < settings.HEIGHT - height - velocity:
        y += velocity
    # Render 
    screen.fill(settings.Colors.BLACK)
    pygame.draw.rect(screen,settings.Colors.GREEN,(x,y,width, height))
    pygame.display.update()
    
pygame.quit()



