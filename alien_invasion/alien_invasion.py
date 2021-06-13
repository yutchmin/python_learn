import sys
import pygame
from setting import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf


def run_game():
	#初始化游戏
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode(
		(ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#设置背景色
	# bg_color = (230,230,230)

	# 创建一艘飞船、一个用于存储子弹的编组和一个外星人编组
	ship = Ship(ai_setting,screen)
	bullets = Group()
	aliens = Group()
	#创建一个外星人
	#alien = Alien(ai_setting, screen)
	#创建外星人群
	gf.create_fleet(ai_setting,screen,ship,aliens)

	#开始游戏主循环
	while 1:
		#监视鼠标和键盘事件
		gf.check_events(ai_setting, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
		gf.update_aliens(ai_setting,ship,aliens)
		# gf.create_fleet(ai_setting,screen,ship,aliens)
		gf.update_screen(ai_setting,screen,ship,aliens,bullets)
		# gf.update_screen(ai_setting, screen, ship,aliens, bullets)

		#每次循环重新绘制屏幕
		# 让最近绘制的屏幕可见
		gf.update_screen(ai_setting,screen,ship,aliens,bullets)



run_game()