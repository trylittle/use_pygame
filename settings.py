
import pygame

class Setting():

    def __init__(self):
        #无须传入screen，因为该类无须需要屏幕
        #----设置大屏幕的宽度
        self.screen_width = 900
        self.screen_height = 600 #设置screen宽和高
        self.screen_color = (255,255,255) #灰色背景创建
        self.shipmoving_speed = 1.5

        #ship的速度设计
        #self.ship_setspeed = 1.5
