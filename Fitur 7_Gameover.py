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


 show_score(1, white, 'consolas', 20)
 pygame.display.update()
 fps_controller.tick(difficulty)