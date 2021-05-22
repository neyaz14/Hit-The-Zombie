# its one kind of shooting game.  You have to tap on  your sreen . And finally if you can hit these zombie by the egg
# and can kill the all zombie you will win.        This game is designed and developed by Neyaz Morshid.

import pygame

screen_size = [360, 530]

screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('background.png')

chicken = pygame.image.load('chicken.png')
winer = pygame.image.load('winer.png')

useru = ['user00.png', 'user001.png', 'user003.png', 'user004.png', 'user005.png', 'user01.png', 'user.png',
         'user2nd.png', 'user3rd.png', 'user4th.png', 'user6th.png', 'user7th.png', 'user8th.png', 'user10th.png' ]
u_index = 0
user = pygame.image.load(useru[u_index])
user_x = 140
move_direction = 'right'

egg = pygame.image.load('egg.png')
egg_y = 50
fired = False

clock = pygame.time.Clock()
keep_alive = True
while keep_alive:
    # mouse event adding code
    x = 0
    y = 0
    screen.blit(background, [x, y])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if background.get_rect().collidepoint(x, y):
                fired = True
            # ----------------------------------------------------

    # egg animation code
    if fired is True:
        egg_y = egg_y + 5
        if egg_y == 480:
            fired = False
            egg_y = 50
    # ----------------------------------------------------

    screen.blit(egg, [146, egg_y])
    screen.blit(chicken, [97, 29])
    # ----------------------------------------------------

    # user animation code
    if move_direction == 'right':
        user_x = user_x + 5
        if user_x == 290:
            move_direction = 'left'
    else:
        user_x = user_x - 5
        if user_x == 0:
            move_direction = 'right'

    screen.blit(user, [user_x, 390])
    # ----------------------------------------------------
    # collosion code
    if egg_y > 398 and 120 < user_x < 170:
        u_index = u_index + 1
        if u_index < len(useru):
            user = pygame.image.load(useru[u_index])
            user_x = 10
        else:
            print(screen.blit(winer, [15, 200]))
            keep_alive = True
        # ----------------------------------------------------
    pygame.display.update()
    clock.tick(60)


