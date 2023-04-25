import pygame
import numpy as np
import simpleaudio as sa

from constants import *


def draw_score_and_time(screen, score, font, time_remaining):
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    time_text = font.render(f'Time: {time_remaining}', True, WHITE)
    time_text_rect = time_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(time_text, time_text_rect)

def play_beep(frequency=440, duration=0.1, volume=0.1):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    audio = tone * (2**15 - 1) / np.max(np.abs(tone))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

def display_game_over(screen, font):
    game_over_text = font.render("GAME OVER", True, WHITE)
    play_again_text = font.render("Press Enter to Play Again or Esc to Quit", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
    screen.blit(game_over_text, game_over_rect)
    screen.blit(play_again_text, play_again_rect)
    pygame.display.flip()
