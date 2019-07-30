import sys
from settings import Settings
from ship import Ship
import pygame

def run_game():
    #初始化游戏并建立一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    #设置背景色
    bg_color = (230, 230, 230)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()