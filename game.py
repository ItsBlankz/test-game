#documentation has everything pls read it if any problem https://www.pygame.org/docs/
import pygame

#Inititalising PyGame
pygame.init()

#All Variables
screen = pygame.display.set_mode((800,400))         #Starting a display Surface
pygame.display.set_caption("game.py")         #changing the title of the window
clock = pygame.time.Clock()         #initialising a clock object to set the framerate
font = pygame.font.Font("font/Pixeltype.ttf",50)       #making a font syntax: pygame.font.Font(path to font or None (for default font), font size)
game_active = True

#Backgrounds
sky_surface = pygame.image.load("graphics\Sky.png")         #import the Sky.png and make a surface of it
ground_surface = pygame.image.load("graphics\ground.png")

#Text
text_surface = font.render('My Game', False, 'Black')       #renders the given text and makes it into a surface, syntax: font_variable.render('Text(str), Anti-Alising(True/False), Colour(from the docs))
text_rect = text_surface.get_rect(center = (400,50))

#Snail 
snail_surface = pygame.image.load('graphics\snail\snail1.png')
snail_rect = snail_surface.get_rect(midbottom = (700,300))

#Player
player_surf = pygame.image.load('graphics\Player\player_walk_1.png')
player_rect = player_surf.get_rect(midbottom = (80,300))            #making a variable for the rectangle, syntax: surface_name.get_rect(name of point(https://imgur.com/a/HQ5g2Nc) = (co-ords))
player_gravity = 0

#End Game msg
end_game_msg = font.render('You Died', False, 'White')
end_game_msg_rect = end_game_msg.get_rect(center = (400,200))

while True:         #starting an event loop to check for events such as close, minimize etc
    for event in pygame.event.get():        #for loop for checking all the events from pygame
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

        # if event.type == pygame.MOUSEMOTION:            #pygame.MOUSEMOTION return (x,y) of the mouse in a tuple, it returns the position only if the cursor is in motion
        #     if player_rect.collidepoint(event.pos):
        #         print('Collision')

        # if event.type == pygame.MOUSEBUTTONDOWN:            #returns true when the mouse button is in the DOWN position i.e when the mouse is clicked
        #     print('Mouse Button Clicked')

        # if event.type == pygame.MOUSEBUTTONUP:          #returns true when the mouse is in the UP position i.e after the click
        #     print('Click Finished')
        if game_active:
            if event.type == pygame.KEYDOWN:                #returns true when ANY key is in the down position; same thing can be done with pygame.KEYUP
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:             #checks if the pressed key is a SPACE
                    player_gravity = -20
                    # setting gravity to -15 if space is pressed, we are setting it to -15 cause when we 
                    # increase it on line 65 the value of y axis decreases which cause it to go up then after 
                    # it crosses 0 the value of y axis starts increasing which drops the player down
        else:
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                                                
    if game_active:
        screen.blit(sky_surface,(0,0))          #Puts the specified regular surface on the display surface, syntax: name_of_display_surface.blit(name_of_regular_surface,(position as a tuple))
        
        screen.blit(ground_surface,(0,300))
        
        pygame.draw.rect(screen,'#c0e8ec',text_rect)            #put the hexadecimal colour code as a STRING
        pygame.draw.rect(screen,'#c0e8ec',text_rect,10)         #syntax: pygame.draw.rect(display_surface,colour,surface,width)
        screen.blit(text_surface, text_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
        # pygame.draw.line(screen,'Black',(0,0),(800,400),10)         #draws a line from start_pos to end_pos, syntax: pygame.draw.line(display surface, color, start_pos,end_pos,width of the line)

        # if player_rect.colliderect(snail_rect):         #returns true when rect1 is colliding with rect2, syntax: rect1.colliderect(rect2)
        #     print('True')

        #Another way to get Position of Mouse
        # mouse_pos = pygame.mouse.get_pos()            #pygame.mouse.get_pos() returns a tuple with the x and y pos of mouse it updates in real-time and doesnt depend if the cursor is moving or not
        # if snail_rect.collidepoint(mouse_pos):
        #     print('Snail Collision')

        #Another way to get mouse pressed
        # mouse_pressed = pygame.mouse.get_pressed()          #pygame.mouse.get_pressed() returns a tuple with 3 boolean values (Left Mouse Click, Middle Mouse Click, Right Mouse Click)
        # if mouse_pressed == (True,False,False):
        #     print("Left Mouse Clicked")

        #Another way to get key pressed
        # keys = pygame.key.get_pressed()         #makes a dictionary of all the boolean values of the keys i.e if they are pressed it is stored as 1 and 0 for the vice-versa
        # if keys[pygame.K_SPACE]:            #accesses the dictionary made in the previous line with an index for the key and check if it is true or false key syntax: pygame.name_of_key_from_docs
        #     print('Jump')
    else:
        screen.fill('Black')
        screen.blit(end_game_msg, end_game_msg_rect)

    pygame.display.update()
    clock.tick(60)          #makes sure that the while loop does not run faster than 60 times a second