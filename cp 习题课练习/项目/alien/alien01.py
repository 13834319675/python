import pygame
import sys
import os
# 因导入本地模块位置错误 settings
class Settings():
    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230,230,230)
# 飞机设置的类
class Ship():
    def __init__(self,screen):
        """初始化飞机并设置具体位置"""
        self.screen = screen
        # 加载飞机图片并取得其外接矩形
        self.image = pygame.image.load("img/bigplane.gif")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船都放在屏幕的正中央
        self.rect_centerx = self.screen_rect.centery
        self.rect_bottom = self.screen_rect.bottom

    def blitem(self):
        """在指定为位置制造飞船"""
        self.screen.blit(self.image,self.rect)


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("alien")
    # 创建飞船实例
    ship = Ship(screen)
    # 开始主循环
    while True:
        # 每次循环都重新绘制屏幕
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)

        # 绘制飞船
        ship.blitem()
        # 设置绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
