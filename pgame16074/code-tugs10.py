import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
warna_bg = (12, 12, 12)

pygame.display.set_caption("Hallo APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen,(240, 24, 55),(350,200,),(350, 350), 5)
	pygame.draw.line(screen,(240, 24, 55),(200,350,),(350, 350), 5)
	pygame.draw.line(screen,(240, 24, 55),(350,200,),(200, 200), 5)
	pygame.draw.line(screen,(240, 24, 55),(200,350,),(200, 200), 5)
	pygame.display.flip()
