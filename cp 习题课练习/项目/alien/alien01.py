import pygame
import sys
from .settings import Settings
import os
curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.split(curpath[0])
sys.path.append(rootpath)
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width
                                     ,ai_settings.screen_height)
    pygame.display.set_caption("alien")

    # 开始主循环
    while True:
        # 每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        # 设置绘制的屏幕可见
        pygame.display.flip()

run_game()
