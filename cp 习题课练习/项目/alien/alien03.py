import pygame
import sys
from pygame.sprite import Sprite,Group
class Settings():
    def __init__(self):
        self.screen_width = 1066
        self.screen_height = 688
        self.bg_color = (230,230,230)
        # 设置飞船的移动量
        self.ship_speed_factor = 1.5
        # 设置子弹的属性
        self.bullet_speed_factor = 1
        self.buller_width = 3
        self.buller_height = 15
        self.buller_color = 60,60,60

class Ship():
    def __init__(self,screen,Setting):
        self.Setting = Setting
        self.screen = screen
        self.image = pygame.image.load("img/hero.gif")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的center属性中使用float
        self.center = float(self.rect.centerx)
        # 移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        # 根据移动标识移动飞船的位置
        """if self.moving_right:
            self.rect.centerx +=self.center
        if self.moving_left:
            self.rect.centerx -=self.center
        if self.moving_up:
            self.rect.bottom -=self.center
        if self.moving_down:
            self.rect.bottom +=self.center"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=  self.Setting.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.Setting.ship_speed_factor


        # 更新
        self.rect.centerx = self.center
    def blitem(self):
        self.screen.blit(self.image,self.rect)
# 创建子弹类
class Buller(Sprite):
    """一个队飞机发射子弹管理的类"""
    def __init__(self,setting,screen,ship):
        """在飞船所处的位置建立一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个子弹对象,并设置正确的位置
        self.rect = pygame.Rect(0,0,setting.buller_width,
                                setting.buller_height)
        # 子弹的初始位置等于飞船的初始位置的顶部
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示子弹的位置
        self.y = float(self.rect.y)
        # 颜色和速度
        self.color = setting.buller_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        """向上移动子弹 更新子弹所在的位置的小数值"""
        self.y -= self.speed_factor
        #更新表示子弹的rect
        self.rect.y = self.y

    def draw_buller(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

def chect_events():
    for evevt in pygame.event.get():
        if evevt.type == pygame.QUIT:
            sys.exit()

def chect_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key ==pygame.K_DOWN:
                ship.moving_down = False

def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("alien")
    ship = Ship(screen,setting)
    bullers = Group()
    buller = Buller(setting,screen,ship)

    while True:

        chect_events()
        screen.fill(setting.bg_color)
        chect_event(ship)
        ship.blitem()
        ship.update()
        buller.update()
        buller.draw_buller()
        pygame.display.flip()

if __name__ == '__main__':
    run_game()


