import sys
import pygame
from settings import Settings as setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    pygame.display.init()

    default_setting = setting()

    screen = pygame.display.set_mode((default_setting.screen_width, default_setting.screen_height))
    ship = Ship(default_setting, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(default_setting)
    sb = Scoreboard(default_setting, screen, stats)
    
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(default_setting, screen, "Play")

    # gf.create_fleet(default_setting, screen, ship, aliens)

    stopped = False

    while not stopped:
        screen.fill(default_setting.background)
        ship.blitThis()
        gf.check_event(default_setting, screen, stats, sb, aliens, ship, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(default_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(default_setting, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(default_setting, screen, stats, sb, ship, aliens, bullets, play_button)
        pygame.display.flip()

    pygame.quit()

run_game()