#创建飞船  并显示在屏幕中央
import pygame
from settings import Setting
class Ship():

    def __init__(self,alien_setting,screen):
        self.screen = screen #已经用了screen,所以下面不用self.screen,而是screen
        #self.image = pygame.display.update('images/ship.bmp')
        self.alien_setting = alien_setting
        self.image = pygame.image.load('image/ship.bmp')
        # self.image = pygame.transform.scale(self.yimage,(90,60))
        self.ship_rect = self.image.get_rect() #如上所述，此处用self.image
        self.screen_rect = screen.get_rect()
        #以上获取了图片和屏幕的大小，为了能够居中显示
        self.ship_rect.center = self.screen_rect.center
        self.ship_rect.bottom = self.screen_rect.bottom
        self.center = float(self.ship_rect.center)

        # self.center = float(''.join(self.ship_rect.center))

        #####yidong
        self.moving_right = False

    def ship_moving(self):
        if self.moving_right:
            #self.ship_rect.center += 1
            self.center += self.alien_setting.shipmoving_speed

        #更新x坐标
        self.ship_rect.center = self.center


    #绘制飞船
    def blitme(self):
        #屏幕上指定位置绘制飞船
        self.screen.blit(self.image,self.ship_rect) #定义了另一个函数，然后需要重新写上self



