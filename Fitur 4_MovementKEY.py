direction = 'RIGHT'
change_to = direction 


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