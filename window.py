import tkinter as tk
from tkinter import ttk

import pygame


def add_text_and_image_about_us(about_us):
    about_us_text = """
    MoodMusic - це програма, яка автоматично підбирає та змінює музику з урахуванням настрою користувача, 
    надаючи можливість створювати персональні плейлисти та налаштовувати музичний супровід у реальному часі 
    для максимальної музичної гармонії зі своїми емоціями і потребами.
    """
    about_us_label = tk.Label(about_us, text=about_us_text, wraplength=600, font=("Helvetica", 14))
    about_us_label.pack()

    image_path = r"images/mood_two.png"
    image = tk.PhotoImage(file=image_path)
    resized_image = image.subsample(1)
    image_label = tk.Label(about_us, image=resized_image)
    image_label.image = resized_image
    image_label.pack()

    return resized_image


def add_audio_controls(change_audiofile, image1, image2, image3, image4, radio_selection, select_file, var, convert_audio, pause_music, unpause_music, stop_music):
    global convert_button

    style = ttk.Style()
    style.configure('Custom.TButton', foreground='#000000', background='#5e34ab', font=('Helvetica', 12), padding=8)

    file_label = tk.Label(change_audiofile, text="Виберіть MP3 файл:", font=('Helvetica', 14))
    file_label.pack(pady=10)

    select_button = ttk.Button(change_audiofile, text="Вибрати файл", command=select_file, style='Custom.TButton')
    select_button.pack(pady=5)

    mood_label = tk.Label(change_audiofile, text="Виберіть настрій:", font=('Helvetica', 14))
    mood_label.pack(pady=10)

    var.set(None)

    radio_frame = tk.Frame(change_audiofile)
    radio_frame.pack()
    radio1 = tk.Radiobutton(radio_frame, image=image1, variable=var, value="sad", command=radio_selection)
    radio2 = tk.Radiobutton(radio_frame, image=image2, variable=var, value="happy", command=radio_selection)
    radio3 = tk.Radiobutton(radio_frame, image=image3, variable=var, value="confused", command=radio_selection)
    radio4 = tk.Radiobutton(radio_frame, image=image4, variable=var, value="angry", command=radio_selection)

    radio1.pack(side=tk.LEFT)
    radio2.pack(side=tk.LEFT)
    radio3.pack(side=tk.LEFT)
    radio4.pack(side=tk.LEFT)

    convert_button = ttk.Button(change_audiofile, text="Конвертувати", style='Custom.TButton', state='disabled',
                                command=convert_audio)
    convert_button.pack(pady=10)

    button_frame = tk.Frame(change_audiofile)
    button_frame.pack()

    play_button = ttk.Button(button_frame, text="Відтворити", command=pygame.mixer.music.play, style='Custom.TButton',
                             state='disabled')
    play_button.pack(side=tk.LEFT, padx=5)

    pause_button = ttk.Button(button_frame, text="Пауза", command=pause_music, style='Custom.TButton', state='disabled')
    pause_button.pack(side=tk.LEFT, padx=5)

    unpause_button = ttk.Button(button_frame, text="Продовжити", command=unpause_music, style='Custom.TButton',
                                state='disabled')
    unpause_button.pack(side=tk.LEFT, padx=5)

    stop_button = ttk.Button(button_frame, text="Стоп", command=stop_music, style='Custom.TButton', state='disabled')
    stop_button.pack(side=tk.LEFT, padx=5)

    return play_button, pause_button, unpause_button, stop_button, convert_button