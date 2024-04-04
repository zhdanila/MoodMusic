import os

import pygame
from pedalboard import Pedalboard
from pedalboard_native import Reverb, PitchShift, Chorus, Phaser, Distortion, LowShelfFilter, Delay
from pedalboard_native.io import AudioFile


def sad_convert(output_file, file_index, audio):
    slowed_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * 0.8)
    })

    slowed_audio.export(output_file, format="mp3")

    samplerate = 44100.0
    with AudioFile(output_file).resampled_to(samplerate) as f:
        audio = f.read(f.frames)

    os.remove(output_file)

    board = Pedalboard([
        Reverb(0.45, 0.5, 0.27, 0.35, 0.9, 0.0),
        PitchShift(-2),
    ])

    proccess(file_index, audio, samplerate, board)


def angry_convert(output_file, file_index, audio):
    audio.export(output_file, format="mp3")

    samplerate = 44100.0
    with AudioFile(output_file).resampled_to(samplerate) as f:
        audio = f.read(f.frames)

    os.remove(output_file)

    board = Pedalboard([
        PitchShift(-8),
        Distortion(10),
        Delay(mix=0.2),
        LowShelfFilter(cutoff_frequency_hz=600)
    ])

    proccess(file_index, audio, samplerate, board)


def confused_convert(output_file, file_index, audio):
    slowed_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * 0.7)
    })

    slowed_audio.export(output_file, format="mp3")

    samplerate = 44100.0
    with AudioFile(output_file).resampled_to(samplerate) as f:
        audio = f.read(f.frames)

    os.remove(output_file)

    board = Pedalboard([
        Reverb(0.8),
        PitchShift(-10),
        Phaser(mix=0.2),
        Distortion(0.1)
    ])

    proccess(file_index, audio, samplerate, board)


def happy_convert(output_file, file_index, audio):
    audio = audio.high_pass_filter(300)

    audio = audio.speedup(1.1)

    audio.export(output_file, format="mp3")

    samplerate = 44100.0
    with AudioFile(output_file).resampled_to(samplerate) as f:
        audio = f.read(f.frames)

    os.remove(output_file)

    board = Pedalboard([
        PitchShift(semitones=5),
        Chorus(mix=0.2),
        Phaser(mix=0.15)
    ])

    proccess(file_index, audio, samplerate, board)


def proccess(file_index, audio, samplerate, board):
    file_index += 1
    output_file = f"Project/project_{file_index}.mp3"

    effected = board(audio, samplerate)

    with AudioFile(output_file, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

    pygame.mixer.music.load(output_file)
    music_playing = False