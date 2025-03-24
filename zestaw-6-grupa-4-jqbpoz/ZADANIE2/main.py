import pygame, sys

pygame.init()

def main():
	clock = pygame.time.Clock()

	pygame.display.set_caption('Zadanie 1 - piłka i grawitacja!')
	icon = pygame.image.load('favicon.ico')
	pygame.display.set_icon(icon)

	pygame.mixer.music.load(r'music.mp3')
	pygame.mixer.music.play(-1)

	size = width, height = 800, 800
	screen = pygame.display.set_mode(size)

	speed = [0, 0]
	accel = [0, 0.5]

	image = pygame.image.load(r'moon.jpg')
	image = pygame.transform.scale(image, size)

	surf_center = (
		(width - image.get_width()) / 2,
		(height - image.get_height()) / 2
	)

	screen.blit(image, surf_center)
	ball = pygame.image.load('ball.gif')
	ball = pygame.transform.scale(ball, (ball.get_width() // 2, ball.get_height() // 2))

	screen.blit(ball, (width / 2, height / 2))

	ballrect = ball.get_rect(center=(width / 2, height / 2))
	pygame.display.flip()


	font = pygame.font.Font(None, 36)

	while True:
		clock.tick(60)
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			sys.exit()

		if keys[pygame.K_UP]:
			speed[1] -= 1
		elif keys[pygame.K_DOWN]:
			speed[1] += 1
		elif keys[pygame.K_LEFT]:
			speed[0] -= 1
		elif keys[pygame.K_RIGHT]:
			speed[0] += 1

		speed[1] += accel[1]


		ballrect = ballrect.move(speed)


		if ballrect.left < 0:
			ballrect.left = 0
			speed[0] = -speed[0]  # odbicie od lewej
		if ballrect.right > width:
			ballrect.right = width
			speed[0] = -speed[0]  # odbicie od prawej
		if ballrect.top < 0:
			ballrect.top = 0
			speed[1] = -speed[1]  # odbicie od górnej
		if ballrect.bottom > height:
			ballrect.bottom = height
			speed[1] = -speed[1]  # odbicie od dolnej

		# Rysowanie tła i piłki
		screen.blit(image, surf_center)
		screen.blit(ball, ballrect)

		# Tworzenie tekstu z bieżącymi wartościami prędkości
		speed_text = font.render(f"Speed X: {speed[0]:.2f} | Speed Y: {speed[1]:.2f}", True, (255, 255, 255))
		screen.blit(speed_text, (10, 10))  # Pozycja tekstu: w lewym górnym rogu ekranu

		# Aktualizacja ekranu
		pygame.display.flip()

if __name__ == '__main__':
	main()
	pygame.quit()
	sys.exit()
