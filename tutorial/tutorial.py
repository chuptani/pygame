import pygame
from sys import exit


pygame.init()

# just to know (ms)
current_time = pygame.time.get_ticks()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png')

bg_surface = pygame.Surface((width,height))
bg_rect = bg_surface.get_rect(top=0)
bg_surface.fill((94,129,162))
bg_alpha = -20
bg_change = 0.3


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))
snail_hitbox = snail_rect.inflate(-12, -5)
snail_hitbox.x -= 2
snail_hitbox.bottom = 300

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_hitbox = player_rect.inflate(-18, 0)
player_hitbox.bottom = 300
player_hitbox.x += 2

game_over_font = pygame.font.Font('font/Pixeltype.ttf', 100)
game_over_text = game_over_font.render("GAME OVER!", False, 'Red3').convert()
game_over_rect = game_over_text.get_rect(centerx = width//2, centery = (height//2) - 25)
game_over_border = game_over_rect.inflate(10, 5)
game_over_border.y -= 9
game_over_border.x -= 2

player_gravity = 0
score = 0
game = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravity = -15
        else :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    game = True


    if game :
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))


        if 0 > snail_rect.x > -72 :
            snail_rect.x -= 5
            screen.blit(snail_surface, (800 + snail_rect.x, 264))
        elif snail_rect.x <= -72 :
            snail_rect.x = 728
            score += 1
        else :
            snail_rect.x -= 5
        snail_hitbox = snail_rect.inflate(-12, -5)
        snail_hitbox.x -= 2
        snail_hitbox.bottom = snail_rect.bottom
        screen.blit(snail_surface, snail_rect)
        # pygame.draw.rect(screen, 'Red3', snail_hitbox, 1)

        player_rect.bottom += player_gravity
        player_gravity += 1
        if player_rect.bottom >= 300 :
            player_rect.bottom = 300
        player_hitbox = player_rect.inflate(-18, 0)
        player_hitbox.bottom = player_rect.bottom
        player_hitbox.x += 2
        screen.blit(player_surf, player_rect)
        # pygame.draw.rect(screen, 'Red3', player_hitbox, 1)


        if player_hitbox.colliderect(snail_hitbox):
            game = False

    else:
        bg_surface.set_alpha(bg_alpha) # type:ignore
        screen.blit(bg_surface, bg_rect)

        if bg_alpha < 255:
            bg_alpha += bg_change

        pygame.draw.rect(screen, 'Black', game_over_border, border_radius = 10)
        screen.blit(game_over_text, game_over_rect)

    score_surf = test_font.render(f"Score : {score}", False, 'White').convert()
    score_rect = score_surf.get_rect(centerx = width//2, top = 10)
    score_border = score_rect.inflate(10, 5)
    score_border.y -= 5
    score_border.x -= 2
    pygame.draw.rect(screen, 'Black', score_border, border_radius = 10)
    screen.blit(score_surf, score_rect)

    pygame.display.update()
    clock.tick(60)
