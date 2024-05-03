# MoodMusic

MoodMusic is an application designed to enhance your music listening experience by applying effects such as Reverb, Delay, Flanger, and more to change the emotional state of songs. 

## Getting Started

### Prerequisites

Before running this project, you need to download and install ffmpeg. Follow these steps:

1. Download ffmpeg from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the downloaded file and rename the extracted folder to `FFmpeg`.
3. Move the `FFmpeg` folder to a desired location (e.g., disk C or another location).
4. Open Command Prompt as an administrator.
5. Add FFmpeg to your system path by running the following command:

   ```
   setx /m PATH "C:\ffmpeg\bin;%PATH%"
   ```

   Replace `C:\ffmpeg\bin` with the actual path where you placed the `FFmpeg` folder.

### Running the Project

1. Clone this repository to your local machine.
2. Open the project in your preferred IDE or code editor.
3. Ensure that ffmpeg is properly installed and added to your system path.
4. Build and run the project to start using MoodMusic.

## Features

- Apply various effects like Reverb, Delay, Flanger, etc., to songs.
- Customize the intensity and settings of each effect.
- Save modified songs to your library.
- Share your favorite modified songs with friends.
- Also, have opportunity to listen to playlists of songs with Deezer API.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, feel free to [create an issue](link_to_issues) or [submit a pull request](link_to_pull_requests).
