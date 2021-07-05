import math
import pygame, sys
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)


class Pen():
    def __init__(self, screen):
        self.color = None  # 画笔的颜色
        self.size = None  # 画笔的大小
        self.last_pos = None  # 上次的画笔的位置
        self.statue = False  # 画笔的状态（落下or抬起）
        self.screen = screen  # 显示屏幕

    def setPenColor(self, color):
        self.color = color

    def setPenSize(self, size):
        self.size = size

    def getPenColor(self):
        return self.color

    def setPenStatue(self, value):
        self.statue = value

    def getPenStatue(self):
        return self.statue

    def getPenSize(self):
        return self.size

    def start_draw(self, pos):
        self.last_pos = pos

    def end_draw(self):
        self.last_pos = None

    def draw(self, pos):
        for point in self.get_points(pos):
            pygame.draw.rect(self.screen, self.color, (point[0], point[1], self.size, self.size))
        self.last_pos = pos

    # 得到上次落笔位置和当前落笔位置之间所有的像素点
    def get_points(self, pos):
        points = [(self.last_pos[0], self.last_pos[1])]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for i in range(int(length)):
            points.append(
                (points[-1][0] + step_x, points[-1][1] + step_y))
        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)
        return set(points)


class Menu:
    def __init__(self, screen, pen):
        self.screen = screen  # 显示屏幕
        self.pen = pen  # 画笔
        self.size = 5  # 画笔的大小
        self.color = [127, 127, 127]  # 画笔的大小
        self.ADD = pygame.image.load('1 (2).jpg')  # 加载增加画笔大小的按钮图片
        self.DE = pygame.image.load('2 (2).jpg')  # 加载减少画笔大小的按钮图片

    # 创建颜色控制区域
    def create_scales(self):
        self.red_scale_surface = pygame.surface.Surface((300, 33))
        self.green_scale_surface = pygame.surface.Surface((300, 33))
        self.blue_scale_surface = pygame.surface.Surface((300, 33))
        for x in range(300):
            c = int((x / 300.) * 255.)
            red = (c, 0, 0)
            green = (0, c, 0)
            blue = (0, 0, c)
            line_rect = Rect(x, 0, 1, 33)
            pygame.draw.rect(self.red_scale_surface, red, line_rect)
            pygame.draw.rect(self.green_scale_surface, green, line_rect)
            pygame.draw.rect(self.blue_scale_surface, blue, line_rect)
        self.red_rect = pygame.Rect(0, 0, 300, 33)
        self.green_rect = pygame.Rect(0, 33, 300, 33)
        self.blue_rect = pygame.Rect(0, 66, 300, 33)
        self.Add_rect = pygame.Rect(300, 20, 32, 32)
        self.De_rect = pygame.Rect(350, 20, 32, 32)

    # 将按钮控件添加到主显示屏幕
    def drawMenu(self):
        self.create_scales()
        self.screen.blit(self.red_scale_surface, (0, 0))
        self.screen.blit(self.green_scale_surface, (0, 33))
        self.screen.blit(self.blue_scale_surface, (0, 66))
        self.screen.blit(self.ADD, (300, 20))
        self.screen.blit(self.DE, (350, 20))
        for component in range(3):
            pos = (int((self.color[component] / 255.) * 300), component * 33 + 15)
            pygame.draw.circle(self.screen, (255, 255, 255), pos, 10)

    # 检测鼠标点击事件
    def click_on(self, pos):
        x, y = pos[0], pos[1]
        if self.red_rect.collidepoint(pos):  # 点pos是否在red_rect内
            self.color[0] = int(x / 300 * 255.)
        elif self.green_rect.collidepoint(pos):
            self.color[1] = int(x / 300 * 255.)
        elif self.blue_rect.collidepoint(pos):
            self.color[2] = int(x / 300 * 255.)
        elif self.Add_rect.collidepoint(pos):
            self.size += 2
        elif self.De_rect.collidepoint(pos):
            self.size -= 2
        self.setPen()

    def setPen(self):
        if self.size > 32:
            self.size = 32
        elif self.size < 5:
            self.size = 5
        self.pen.setPenColor(self.color)
        self.pen.setPenSize(self.size)


class paniter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.pen = Pen(self.screen)
        self.pen.setPenColor(BLUE)
        self.pen.setPenSize(5)
        self.pen.setPenStatue(False)  # 画笔放下或抬起
        self.menu = Menu(self.screen, self.pen)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("绘画板")

    def run(self):
        self.screen.fill(WHITE)
        pygame.draw.line(self.screen, GREEN, (0, 100), (400, 100), 2)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:  # 键盘事件
                    if event.key == K_ESCAPE:
                        self.screen.fill(WHITE)
                        pygame.draw.line(self.screen, GREEN, (0, 100), (400, 100), 2)
                elif event.type == MOUSEBUTTONDOWN:  # 鼠标事件
                    pos = event.pos
                    if pos[1] > 100:  # 鼠标点击区域在画布区域
                        self.pen.setPenStatue(True)
                        self.pen.start_draw(event.pos)
                    else:  # 鼠标点击区域在菜单区域
                        self.menu.click_on(pos)
                elif self.pen.getPenStatue() and event.type == MOUSEBUTTONUP:  # 画笔抬起
                    self.pen.setPenStatue(False)
                    self.pen.end_draw()
                elif self.pen.getPenStatue() and event.type == MOUSEMOTION:
                    self.pen.draw(event.pos)
            self.menu.drawMenu()
            pygame.display.update()
            self.clock.tick(30)  # 刷帧率


def main():
    app = paniter()
    app.run()


main()