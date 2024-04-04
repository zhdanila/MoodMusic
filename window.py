import tkinter as tk

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
