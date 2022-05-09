import pygame

pygame.init()

surface = pygame.display.set_mode((500, 400))

fondo = (39, 32, 74)
piso = (72, 97, 135)
caja = (128, 188, 197)

pygame.draw.rect(surface, fondo, pygame.Rect(0, 0, 500, 400))
pygame.draw.rect(surface, piso, pygame.Rect(0, 260, 500, 500))
pygame.draw.rect(surface, caja, pygame.Rect(125, 120, 250, 200))


imagen = pygame.image.load('sprite1.png').convert_alpha()

surface.blit(imagen, (200,180))
pygame.display.update()
