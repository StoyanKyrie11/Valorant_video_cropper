# Valorant cropper

Overview -- project for formatting original Valorant game videos by choosing respective Valorant gameplay round video files, then proceed with cropping, resizing and archiving them in respective Output folder within the parent directory.

## Requirements

- Python >= 3.8
- FFmpeg installed (follow guide in: https://www.wikihow.com/Install-FFmpeg-on-Windows)

## Setup

Run below in a cmd console or terminal.

1. Git clone the repo.
2. Cd into the folder.
3. `python -m venv venv`
4. `venv\scripts\activate` (windows) or `source venv/bin/activate` (mac/linux).
5. `pip install -r requirements.txt`.

- Hit `deactivate` to get out of venv

## Execution

1. Cd into the folder.
2. `venv\scripts\activate` (windows) or `source venv/bin/activate` (mac/linux).
3. `python -m cropper`.
4. Follow the instructions in the gui and watch out any error prompted in console.

- Hit `Ctrl C` to interrupt execution.
- Hit `deactivate` to get out of venv
