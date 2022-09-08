# coding:utf-8

#主程序，完成飞船打外星人,【可以在终端上下载pygame】
import pygame
import  sys
from settings import Setting
from ship import Ship
import functions as fc
def run_game():
    pygame.init() #初始化pygame
    #创建screen
    alien_setting = Setting() #实例化
    screen = pygame.display.set_mode((alien_setting.screen_width,alien_setting.screen_height))#主程序中创建screen
    ######set_mode是元组！！！！
    pygame.display.set_caption('飞船打外星人') #创建标题
    ship =Ship(alien_setting,screen) #绘制飞船

    while True:
        fc.check_event(ship)
        ship.ship_moving() #实例下的方法，就点即可
        ###更新屏幕
        fc.update_screen(alien_setting,screen,ship)
        # screen.fill((alien_setting.screen_color))#是屏幕背景色，而不是pygame
        # ship.blitme()#绘制船
        # pygame.display.flip()#屏幕更新

run_game()
