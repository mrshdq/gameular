import pygame, sys, time, random

pygame.init()
difficulty = 10

frame_size_x = 720
frame_size_y = 480

pygame.display.set_caption('Game Ular')
screen = pygame.display.set_mode((frame_size_x, frame_size_y))

start_img = pygame.image.load('img/start.png')

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

def draw_start_menu():
    screen.blit(start_img, (0, 0))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def draw_difficulty_menu():
    screen.fill(black)
    my_font = pygame.font.SysFont('times new roman', 40)
    easy_surface = my_font.render('1. Easy', True, white)
    medium_surface = my_font.render('2. Medium', True, white)
    hard_surface = my_font.render('3. Hard', True, white)
    harder_surface = my_font.render('4. Harder', True, white)
    impossible_surface = my_font.render('5. Impossible', True, white)

    screen.blit(easy_surface, (frame_size_x / 2 - easy_surface.get_width() / 2, frame_size_y / 2 - 100))
    screen.blit(medium_surface, (frame_size_x / 2 - medium_surface.get_width() / 2, frame_size_y / 2 - 50))
    screen.blit(hard_surface, (frame_size_x / 2 - hard_surface.get_width() / 2, frame_size_y / 2))
    screen.blit(harder_surface, (frame_size_x / 2 - harder_surface.get_width() / 2, frame_size_y / 2 + 50))
    screen.blit(impossible_surface, (frame_size_x / 2 - impossible_surface.get_width() / 2, frame_size_y / 2 + 100))
    
    pygame.display.flip()
    selecting = True
    global difficulty
    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == ord('1'):
                    difficulty = 10
                    selecting = False
                if event.key == ord('2'):
                    difficulty = 20
                    selecting = False
                if event.key == ord('3'):
                    difficulty = 30
                    selecting = False
                if event.key == ord('4'):
                    difficulty = 40
                    selecting = False
                if event.key == ord('5'):
                    difficulty = 50
                    selecting = False

def game_over():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sound/Gameover.mp3')
    pygame.mixer.music.play()

    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(15)
    pygame.quit()
    sys.exit()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    screen.blit(score_surface, score_rect)

draw_start_menu()
draw_difficulty_menu()

pygame.mixer.music.load('sound/Backsound.mp3')
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, ord('w')] and direction != 'DOWN':
                change_to = 'UP'
            if event.key in [pygame.K_DOWN, ord('s')] and direction != 'UP':
                change_to = 'DOWN'
            if event.key in [pygame.K_LEFT, ord('a')] and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key in [pygame.K_RIGHT, ord('d')] and direction != 'LEFT':
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    food_spawn = True

    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(difficulty)
