import pygame
from environment import Environment

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

env = Environment()
running = True
env.reset()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    env.step([1, -1])  # movimento bobo só pra testar
    env.render(screen)
    clock.tick(30)

pygame.quit()
