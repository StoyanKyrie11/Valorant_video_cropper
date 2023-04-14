
import os
import time
from dataclasses import dataclass
from typing import List

from moviepy.editor import VideoFileClip
from moviepy.video.fx.crop import crop


def crop_files(file_path: str, destination_folder: str) -> str:
    """Function designed to instantiate VideoClip object, resize, clip and format the initial video, output the final outcome video."""

    # Create axis constant coordinates;display width and height location of the video map; preset value; output folder name.
    X1, Y1, X2, Y2 = 50, 50, 80, 80
    WIDTH, HEIGHT = 376, 376
    ULTRAFAST = 'ultrafast'

    clip = VideoFileClip(file_path).without_audio()
    cropped_clip_two = crop(clip, x1=X1, y1=Y1, x2=X2, y2=Y2, width=WIDTH, height=HEIGHT)
    # Pause for a second - leave time for Multiprocessing logic to grab another process from the pool.
    time.sleep(1)

    # Saving cropped .mp4 video in respective folder
    cropped_final_clip = cropped_clip_two.write_videofile(f"{destination_folder}/{os.path.basename(file_path)}", preset=ULTRAFAST)
    # Flush memory, close object.
    clip.close()

    # Return each cropped video file value.
    return str(cropped_final_clip)


@dataclass
class StateManager:
    
    files_to_load: List[str]
    output_dir: str = None
    output_zip_name: str = None
