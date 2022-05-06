import pygame
pygame.init()
surface = pygame.display.set_mode((600, 400))

amarillo = (254,238,129)
azul = (45,65,162)
rojo = (227,49,45)
verde = (55,159,107)
cafe = (138,89,77)
celeste = (111,214,236)

pygame.draw.rect(surface, celeste, pygame.Rect(0, 0, 600, 400))
pygame.draw.rect(surface, verde, pygame.Rect(0, 300, 600, 100))
pygame.draw.rect(surface, amarillo, pygame.Rect(100, 200, 250, 150))
pygame.draw.rect(surface, celeste, pygame.Rect(230, 220, 90, 50))
pygame.draw.rect(surface, azul, pygame.Rect(140, 250, 70, 100))
pygame.draw.rect(surface, cafe, pygame.Rect(450, 200, 60, 150))
pygame.draw.polygon(surface, rojo, ((100,200),(225,100),(350,200)))
pygame.draw.circle(surface, verde,(480, 150), 75)
pygame.display.flip()



pygame.mouse.set_cursor(*pygame.cursors.arrow)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    pygame.display.update()

## El codigo para conseguir las coordenadas del mouse fue extraido de: https://stackoverflow.com/questions/64284668/pygame-mouse-clicks-not-getting-detected

