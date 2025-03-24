import pygame
from random import randint

pygame.init()

# Kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)
ZIELONY = (0, 255, 0)

# Ustawienia ekranu
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong Solo")

# Czcionki
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

# Klasa Rakietka
class Rakietka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > size[0] - self.rect.width:
            self.rect.x = size[0] - self.rect.width

# Klasa Pilka
class Pilka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(-4, 4), randint(4, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8, 8)

# Funkcja menu

def menu():
    screen.fill(NIEBIESKI)
    title = font_large.render("PING PONG", True, BIALY)
    instructions = font_small.render("Press Enter to play!!!", True, BIALY)
    screen.blit(title, (size[0] // 2 - title.get_width() // 2, 150))
    screen.blit(instructions, (size[0] // 2 - instructions.get_width() // 2, 250))
    pygame.display.flip()

    in_menu = True
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                in_menu = False

# Funkcja końca gry
def game_over(score, best_score):
    screen.fill(CZERWONY)
    game_over_text = font_large.render("Game Over", True, BIALY)
    score_text = font_small.render(f"Your Score: {score}", True, BIALY)
    best_score_text = font_small.render(f"Best Score: {best_score}", True, BIALY)
    instructions1 = font_small.render("Press Enter to play again", True, BIALY)
    instructions2 = font_small.render("Press Escape to exit", True, BIALY)

    screen.blit(game_over_text, (size[0] // 2 - game_over_text.get_width() // 2, 100))
    screen.blit(score_text, (size[0] // 2 - score_text.get_width() // 2, 200))
    screen.blit(best_score_text, (size[0] // 2 - best_score_text.get_width() // 2, 250))
    screen.blit(instructions1, (size[0] // 2 - instructions1.get_width() // 2, 320))
    screen.blit(instructions2, (size[0] // 2 - instructions2.get_width() // 2, 370))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Główna funkcja gry
def game():
    rakietka = Rakietka(ZIELONY, 100, 10)
    rakietka.rect.x = 300
    rakietka.rect.y = 490

    pilka = Pilka(BIALY, 10, 10)
    pilka.rect.x = randint(50, 650)
    pilka.rect.y = 50

    all_sprites = pygame.sprite.Group()
    all_sprites.add(rakietka)
    all_sprites.add(pilka)

    score = 0
    try:
        with open("best_score.txt", "r") as file:
            best_score = int(file.read())
    except:
        best_score = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rakietka.move_left(5)
        if keys[pygame.K_RIGHT]:
            rakietka.move_right(5)

        pilka.update()

        if pilka.rect.y > size[1]:
            running = False

        if pygame.sprite.collide_rect(pilka, rakietka):
            pilka.bounce()
            score += 1
            if score > best_score:
                best_score = score

        if pilka.rect.x <= 0 or pilka.rect.x >= size[0] - pilka.rect.width:
            pilka.velocity[0] = -pilka.velocity[0]
        if pilka.rect.y <= 0:
            pilka.velocity[1] = -pilka.velocity[1]

        screen.fill(CZARNY)
        all_sprites.draw(screen)

        score_text = font_small.render(f"Score: {score}", True, BIALY)
        best_score_text = font_small.render(f"Best Score: {best_score}", True, BIALY)
        screen.blit(score_text, (10, 10))
        screen.blit(best_score_text, (10, 35))
        pygame.display.flip()

        clock.tick(60)

    with open("best_score.txt", "w") as file:
        file.write(str(best_score))

    return score, best_score

# Główna pętla programu
while True:
    menu()
    wynik, najlepszy_wynik = game()
    if not game_over(wynik, najlepszy_wynik):
        break