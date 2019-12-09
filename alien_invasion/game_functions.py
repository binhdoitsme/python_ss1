import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

# event loop
def check_event(settings, screen, stats, sb, aliens, ship, bullets, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, stats, sb, aliens, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, aliens, ship, bullets, play_button, mouse_x, mouse_y)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(event, settings, screen, stats, sb, aliens, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.moving_left = False
    elif event.key == pygame.K_LEFT:
        ship.moving_right = False
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        start_game(settings, screen, stats, sb, aliens, ship, bullets)
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_play_button(settings, screen, stats, sb, aliens, ship, bullets, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        start_game(settings, screen, stats, sb, aliens, ship, bullets)
        
def start_game(settings, screen, stats, sb, aliens, ship, bullets):
    if not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

        pygame.mouse.set_visible(False)

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitThis()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    else:
        sb.show_score()

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_limit:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    repopulate(settings, screen, stats, sb, ship, aliens, bullets)

# is called when a level is completed
def repopulate(settings, screen, stats, sb, ship, aliens, bullets):
    # repopulate the fleet
    if len(aliens) == 0:
        # destroy all remaining bullets
        bullets.empty()
        # speed up
        settings.increase_speed()
        # next level
        stats.level += 1
        sb.prep_level()
        # repopulate
        create_fleet(settings, screen, ship, aliens)      

def check_alien_ship_collision(settings, screen, stats, sb, ship, aliens, bullets):
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, stats, sb, ship, aliens, bullets)

def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)
        
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def update_aliens(settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    check_alien_ship_collision(settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets)

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

# check if ship is hit by aliens
def ship_hit(settings, screen, stats, sb, ship, aliens, bullets):
    # empty alien and bullet list
    aliens.empty()
    bullets.empty()

    # create new fleet and center ship
    create_fleet(settings, screen, ship, aliens)
    ship.center_ship()

    if stats.ships_left > 1:
        # Decrement ships_left
        stats.ships_left -= 1
        # Update scoreboard
        sb.prep_ships()
        # # pause
        # sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()