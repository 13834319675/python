import sys
import pygame

def run_ganme():
    # 初始化构建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption("alien")
    bg_color = (230,230,230)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    run_ganme()