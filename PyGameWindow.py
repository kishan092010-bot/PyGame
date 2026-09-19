import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        GREEN = (0,255,0)
        pygame.draw.circle(window, GREEN, (300,300), 50)
        pygame.display.flip()