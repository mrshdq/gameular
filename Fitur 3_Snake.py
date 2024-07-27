snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

 snake_body.insert(0, list(snake_pos))
 if snake_pos == food_pos:
     score += 1
     food_spawn = False
 else:
     snake_body.pop()

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