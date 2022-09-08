
import sys
import pygame

def check_event(ship):#传参
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:#松开按键
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
def update_screen(alien_setting,screen,ship):
    screen.fill((alien_setting.screen_color))  # 是屏幕背景色，而不是pygame
    ship.blitme()  # 绘制船
    pygame.display.flip()  # 屏幕更新