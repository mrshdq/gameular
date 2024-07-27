difficulty = 10 #Default

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
