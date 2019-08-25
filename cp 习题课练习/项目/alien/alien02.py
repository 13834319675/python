import pygame
import sys
# settings类

class Settings():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 768
        self.bg_color = (230,230,230)
# 加载绘制图片\
class Ship():
    def __init__(self,screen):
        """初始化飞机并设置具体位置"""
        self.screen = screen
        # 加载飞机图片并取得其外接矩形
        self.image = pygame.image.load("img/hero.gif")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船都放在屏幕的正中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitem(self,):
        self.screen.blit(self.image,self.rect)
# 检测事件
def chect_events():
    """相应事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# 飞船移动
def check_event(ship):
    """相应按键和鼠标事件"""
    # 判断是否退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 也可以直接使用封装好的函数
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 像右移动
                ship.rect.centerx +=10
            if event.key == pygame.K_LEFT:
                ship.rect.centerx -=10
            if event.key == pygame.K_UP:
                ship.rect.bottom -=10
            if event.key == pygame.K_DOWN:
                ship.rect.bottom +=10

def run_game():
    #开始循环
    setting = Settings()
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_height,setting.screen_width))
    pygame.display.set_caption("Allen")
    ship = Ship(screen)
    while True:
        chect_events()
        screen.fill(setting.bg_color)
        check_event(ship)
        ship.blitem()
        pygame.display.flip()

if __name__ == '__main__':
    run_game()

# 备注明天完善飞船的移动和 修改一下屏幕的长宽