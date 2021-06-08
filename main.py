from engine import Engine
import pygame


if __name__ == "__main__":
    pygame.init()
    engine = Engine(3, 3)
    engine.start()