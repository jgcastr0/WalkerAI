import pygame
import numpy as np

WIDTH, HEIGHT = 800, 400
GRAVITY = 0.5

class BipedalRobot:
    def __init__(self):
        self.body_x = 100
        self.body_y = HEIGHT - 100
        self.body_vx = 0
        self.body_vy = 0

        self.leg_left_angle = 0.0
        self.leg_right_angle = 0.0

    def step(self, action):
        # Action = [delta_angle_left, delta_angle_right]
        self.leg_left_angle += action[0]
        self.leg_right_angle += action[1]

        # Simula movimento simples para frente
        self.body_vx += (np.sin(self.leg_right_angle) + np.sin(self.leg_left_angle)) * 0.2
        self.body_x += self.body_vx
        self.body_y += self.body_vy
        self.body_vy += GRAVITY

        if self.body_y >= HEIGHT - 50:
            self.body_y = HEIGHT - 50
            self.body_vy = 0

    def get_state(self):
        return np.array([self.leg_left_angle, self.leg_right_angle, self.body_vx])

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 255), (self.body_x, self.body_y, 20, 50))  # corpo
        # Desenhar pernas depois

class Environment:
    def __init__(self):
        self.robot = BipedalRobot()
        self.done = False
        self.total_reward = 0

    def reset(self):
        self.robot = BipedalRobot()
        self.done = False
        self.total_reward = 0
        return self.robot.get_state()

    def step(self, action):
        self.robot.step(action)
        reward = self.robot.body_vx  # recompensa: andar pra frente
        self.total_reward += reward

        if self.robot.body_y > HEIGHT - 49:
            self.done = True

        return self.robot.get_state(), reward, self.done

    def render(self, screen):
        screen.fill((255, 255, 255))
        self.robot.draw(screen)
        pygame.display.flip()
