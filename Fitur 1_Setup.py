import pygame, sys, time, random

pygame.init()

frame_size_x = 720
frame_size_y = 480

pygame.display.set_caption('Snake Eater')
screen = pygame.display.set_mode((frame_size_x, frame_size_y))

start_img = pygame.image.load('img/start.png')

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps_controller = pygame.time.Clock() #FPS DEFAULT PYGAME

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

draw_start_menu()