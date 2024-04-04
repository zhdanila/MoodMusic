from tkinter import *
from tkinter import ttk, filedialog
import win32gui
from pydub import AudioSegment
from pedalboard import *
import os
import tkinter as tk
import deezer
import pygame
import random
import io
import aiohttp
import asyncio
import pygame.mixer

import audio_convert
import indexFIle
from window import add_text_and_image_about_us, add_audio_controls

file_index = indexFIle.load_file_index()

root = tk.Tk()
root.title("MoodMusic")
root.geometry("771x477")
root.resizable(False, False)
pygame.init()
pygame.mixer.init()

image1 = tk.PhotoImage(file="images/sad.png")
image2 = tk.PhotoImage(file=r"images/happy.png")
image3 = tk.PhotoImage(file=r"images/confused.png")
image4 = tk.PhotoImage(file=r"images/angr.png")

var = tk.StringVar(value="")

top_frame = tk.Frame(root, bg="#5e34ab", height=100, width=100)
top_frame.pack(side="top", fill="x")

image_path = r"images/logo.png"
image = tk.PhotoImage(file=image_path)
image = image.subsample(3)
logo_label = tk.Label(top_frame, image=image, bg="#5e34ab")
logo_label.pack(expand=True)

notebook = ttk.Notebook(style='Custom.TNotebook')
notebook.pack(expand=True, fill=BOTH)

about_us = ttk.Frame(notebook)
melody_library = ttk.Frame(notebook)
last_project = ttk.Frame(notebook)
change_audiofile = ttk.Frame(notebook)

change_audiofile.pack(fill=BOTH, expand=True)
melody_library.pack(fill=BOTH, expand=True)
last_project.pack(fill=BOTH, expand=True)
about_us.pack(fill=BOTH, expand=True)

notebook.add(change_audiofile, text="Змінити аудіофайл", compound=tk.LEFT)
notebook.add(melody_library, text="Бібліотека мелодій", compound=tk.LEFT)
notebook.add(last_project, text="Останні проєкти", compound=tk.LEFT)
notebook.add(about_us, text="Про нас", compound=tk.LEFT)

style = ttk.Style()
style.configure('Custom.TNotebook.Tab', padding=[31, 8], anchor='center', focuscolor='#5e34ab')

resized_image = add_text_and_image_about_us(about_us)

music_playing = False
file_state = False


def select_file():
    global music_playing, convert_button
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        global file_state
        file_state = True
        check_buttons_state()


def save_file_index():
    with open('file_index.txt', 'w') as file:
        file.write(str(file_index))


def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()


def stop_music():
    pygame.mixer.music.stop()


def unpause_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()


def enable_buttons():
    play_button.config(state='enabled')
    unpause_button.config(state='enabled')
    stop_button.config(state='enabled')
    pause_button.config(state='enabled')


def convert_audio():
    global file_index
    output_file = f"Project/result_{file_index}.mp3"

    pygame.mixer.music.stop()
    if var.get() == "sad":
        audio = AudioSegment.from_file(file_path, format="mp3")
        audio_convert.sad_convert(output_file, file_index, audio)

    elif var.get() == "angry":
        audio = AudioSegment.from_file(file_path, format="mp3")
        audio_convert.angry_convert(output_file, file_index, audio)

    elif var.get() == "confused":
        audio = AudioSegment.from_file(file_path, format="mp3")
        audio_convert.confused_convert(output_file, file_index, audio)

    elif var.get() == "happy":
        audio = AudioSegment.from_file(file_path, format="mp3")
        audio_convert.happy_convert(output_file, file_index, audio)

    play_button.config(state='enabled')
    pause_button.config(state='enabled')
    unpause_button.config(state='enabled')
    stop_button.config(state='enabled')

    save_file_index()


def radio_selection():
    global convert_button

    check_buttons_state()


def check_buttons_state():
    selected_value = var.get()
    if selected_value != "None" and file_state:
        convert_button.config(state='enabled')
    else:
        convert_button.config(state='disabled')


play_button, pause_button, unpause_button, stop_button, convert_button = add_audio_controls(change_audiofile, image1,
                                                                                            image2, image3, image4,
                                                                                            radio_selection,
                                                                                            select_file, var,
                                                                                            convert_audio, pause_music,
                                                                                            unpause_music, stop_music)


def add_to_taskbar():
    hwnd = root.winfo_id()
    win32gui.ShowWindow(hwnd, 5)
    win32gui.SetParent(hwnd, 0)
    root.update_idletasks()


def update_list():
    file_list.delete(0, tk.END)

    global folder_path

    folder_path = os.path.join("Project")

    mp3_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]

    for file in mp3_files:
        file_list.insert(tk.END, file)


style.configure('Custom.TButton', foreground='#000000', background='#5e34ab', font=('Helvetica', 12), padding=8)

update_button = ttk.Button(last_project, text="Оновити список", command=update_list, style='Custom.TButton')
update_button.pack(pady=10)

file_list = tk.Listbox(last_project)
file_list.pack()


def play_selected():
    selected_file = file_list.get(file_list.curselection())
    file_path = os.path.join(folder_path, selected_file)

    pygame.mixer.music.load(file_path)


select_button = ttk.Button(last_project, text="Обрати", command=play_selected, style='Custom.TButton')
select_button.pack(pady=5)

button_frame = tk.Frame(last_project)
button_frame.pack()

play_button_2 = ttk.Button(button_frame, text="Відтворити", command=pygame.mixer.music.play, style='Custom.TButton',
                           state='enabled')
play_button_2.pack(side=tk.LEFT, padx=5)

pause_button_2 = ttk.Button(button_frame, text="Пауза", command=pause_music, style='Custom.TButton', state='enabled')
pause_button_2.pack(side=tk.LEFT, padx=5)

unpause_button_2 = ttk.Button(button_frame, text="Продовжити", command=unpause_music, style='Custom.TButton',
                              state='enabled')
unpause_button_2.pack(side=tk.LEFT, padx=5)

stop_button_2 = ttk.Button(button_frame, text="Стоп", command=stop_music, style='Custom.TButton', state='enabled')
stop_button_2.pack(side=tk.LEFT, padx=5)

add_to_taskbar()

client = deezer.Client(app_id='656531', app_secret='be52f4ba4f5feb9b2f5740650c5b4d1b')

current_track_index = -1
current_tracks = []

paused = False


def pause_track():
    global paused
    pygame.mixer.music.pause()
    paused = True


def resume_track():
    global paused
    pygame.mixer.music.unpause()
    paused = False


def replay_track():
    pygame.mixer.music.rewind()
    pygame.mixer.music.play()


def stop_track():
    pygame.mixer.music.stop()


async def play_random_track():
    global current_tracks, current_track_index
    track_category = category_var.get()

    results = client.search(track_category)

    if results:
        current_tracks = results
        current_track_index = random.randint(0, len(results) - 1)

        try:
            await play_current_track()
        except Exception as e:
            print(f"Помилка при відтворенні треку: {e}")


async def check_music_finished():
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
    pygame.mixer.quit()


async def play_current_track():
    global current_track_index, current_tracks
    if current_track_index != -1 and current_tracks:
        track = current_tracks[current_track_index]
        track_url = track.preview
        track_title = track.title

        print(f"Playing: {track_title}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(track_url) as response:
                    audio_data = io.BytesIO(await response.read())

                    pygame.mixer.init()
                    pygame.mixer.music.load(audio_data)
                    pygame.mixer.music.play()

                    await asyncio.sleep(0.1)
                    asyncio.create_task(check_music_finished())

        except aiohttp.ClientError as e:
            print(f"Помилка під час завантаження аудіо: {e}")


async def start_play_random_track():
    loop = asyncio.get_event_loop()
    await loop.create_task(play_random_track())


def play_next_track():
    global current_track_index
    if current_tracks:
        current_track_index = (current_track_index + 1) % len(current_tracks)
        asyncio.run(play_current_track())


categories = ["relaxed", "workout", "concentration", "depressive", "energetic"]

category_var = tk.StringVar(melody_library)
category_var.set(categories[0])

category_menu = tk.OptionMenu(melody_library, category_var, *categories)
category_menu.config(font=("Helvetica", 14))
category_menu.pack(pady=30)

style = ttk.Style()

style.configure('Custom.TButton', foreground='#000000', background='#5e34ab', font=('Helvetica', 12), padding=8)
play_button_2 = ttk.Button(melody_library, text="Обрати категорію",
                           command=lambda: root.after(0, lambda: asyncio.run(start_play_random_track())),
                           style='Custom.TButton')
play_button_2.pack(pady=5)

next_button = ttk.Button(melody_library, text="Відтворити наступний трек", command=play_next_track,
                         style='Custom.TButton')
next_button.pack(pady=5)

stop_button_3 = ttk.Button(melody_library, text="Зупинити", command=stop_music, style='Custom.TButton')
stop_button_3.pack(pady=5)

root.mainloop()
