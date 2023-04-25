import pygame
import math
import random
from player import Player
from asteroid import create_random_asteroid, create_smaller_asteroids
from utils import play_beep, draw_score_and_time, display_game_over
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minimal Asteroids Game")
    clock = pygame.time.Clock()

    player = Player(WIDTH // 2, HEIGHT // 2)
    projectiles = []
    score = 0

    # Create a list of asteroids
    num_asteroids = 3  # Change this number to create more or fewer asteroids
    asteroids = [create_random_asteroid() for _ in range(num_asteroids)]

    # Initialize font for displaying the score and game over message
    pygame.font.init()
    score_font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 48)

    running = True
    game_over = False
    start_ticks = pygame.time.get_ticks()  # Get the starting ticks when the game starts

    while running:
        clock.tick(60)
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score += player.shoot(projectiles)

            # Update the remaining time and check if the game should end due to the timer
            current_ticks = pygame.time.get_ticks()
            elapsed_time = (current_ticks - start_ticks) // 1000
            remaining_time = max(0, 30 - elapsed_time)
            if remaining_time == 0:
                game_over = True

            keys_pressed = pygame.key.get_pressed()
            player.update(keys_pressed)

            # Update projectiles and remove those that go off-screen
            projectiles = [p for p in projectiles if p.update()]

            for asteroid in asteroids:
                asteroid.update()

            # Check for collisions between projectiles and the asteroids
            projectiles_to_remove = []
            for projectile in projectiles:
                for i, asteroid in enumerate(asteroids):
                    if asteroid.collides_with_projectile(projectile):
                        score += SCORE_PER_HIT
                        projectiles_to_remove.append(projectile)
                        if asteroid.level > 1:
                            asteroids += create_smaller_asteroids(asteroid)
                        if asteroid.level == 3:
                            asteroids[i] = create_random_asteroid()
                        else:
                            asteroids.pop(i)
                        play_beep()
                        break
                else:
                    continue  # executed if the inner loop completed without a break
                break  # executed if the inner loop encountered a break

            for projectile in projectiles_to_remove:
                projectiles.remove(projectile)

            # Check for collisions between the player and the asteroids
            for asteroid in asteroids:
                if player.collides_with_asteroid(asteroid):
                    game_over = True
                    break
                
            screen.fill(BLACK)
            player.draw(screen)

            for projectile in projectiles:
                projectile.draw(screen)

            # Draw all asteroids
            for asteroid in asteroids:
                asteroid.draw(screen)

            time_elapsed = (pygame.time.get_ticks() - start_ticks) // 1000
            time_remaining = max(30 - time_elapsed, 0)
            draw_score_and_time(screen, score, score_font, time_remaining)

        else:
            display_game_over(screen, game_over_font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Restart the game
                        player = Player(WIDTH // 2, HEIGHT // 2)
                        projectiles = []
                        score = 0
                        asteroids = [create_random_asteroid() for _ in range(num_asteroids)]
                        game_over = False
                        start_ticks = pygame.time.get_ticks()  # Reset the starting ticks
                    elif event.key == pygame.K_ESCAPE:
                        running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()

