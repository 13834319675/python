import pygame
import sys

class Settings():
    def __init__(self):
        self.screen_width = 1066
        self.screen_height = 688
        self.bg_color = (230,230,230)
        # 设置飞船的移动量
        self.ship_speed_factor = 1.5

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
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.Setting.ship_speed_factor


        # 更新
        self.rect.centerx = self.center
    def blitem(self):
        self.screen.blit(self.image,self.rect)

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
    while True:
        chect_events()
        screen.fill(setting.bg_color)
        chect_event(ship)
        ship.blitem()
        ship.update()
        pygame.display.flip()

if __name__ == '__main__':
    run_game()


