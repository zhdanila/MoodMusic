import pygame


def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()


def stop_music():
    pygame.mixer.music.stop()


def unpause_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()