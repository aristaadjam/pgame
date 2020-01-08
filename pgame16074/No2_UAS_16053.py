import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
done = True
warna_bg = (222,220,222)
pygame.display.set_caption("GARIS UAS")
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and \
               event.key == pygame.K_ESCAPE:
            done = True
screen.fill(warna_bg)
pygame.draw.line(screen, (250, 0, 0), (100, 0), (100,400))

pygame.draw.line(screen, (250, 0, 0), (200, 0), (200,500))

pygame.draw.line(screen, (250, 0, 0), (300, 0), (300,600))



pygame.draw.line(screen, (250, 0, 0), (0, 100), (400,100))

pygame.draw.line(screen, (250, 0, 0), (0, 200), (600,200))

pygame.draw.line(screen, (250, 0, 0), (0, 300), (700,300))
pygame.display.update()
clock.tick(110)