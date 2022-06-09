import pygame
pygame.init()
display_surface = pygame.display.set_mode((500, 300))

cyan = (120, 230, 240)
black = (0, 0, 0)
 
font = pygame.font.Font('freesansbold.ttf', 30)

text = font.render('Contador = 0', True, black)
textRect = text.get_rect()
textRect.center = (100, 30)

while True:
    
    display_surface.fill(cyan)
    display_surface.blit(text, textRect)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
        pygame.display.update()
