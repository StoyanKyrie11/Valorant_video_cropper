from typing import List
from functools import partial
import time
import multiprocessing

import tkinter as tk
from tkinter import Tk, Button, filedialog, simpledialog

from .core import crop_files, StateManager
from .utils import zip_directory


def file_dialog() -> List[str]:
    """Function to prompt user for input multiple video files as input to be formatted."""

    # Initiate tkinter file/folder dialog window.
    root = tk.Tk()
    # Call the object.
    root.withdraw()

    # Save all passed file names after dialog window closes in a list variable.
    file_path = filedialog.askopenfilenames()

    # Return list of file paths.
    return list(file_path)


def get_zip_file_name(content: Tk, states: StateManager) -> str:
    """Function creating a dialog box for inputting user-customized .zip file name."""

    # Create variable from simple dialog object to hold dialog box.
    states.output_dir = filedialog.askdirectory()
    states.output_zip_name = simpledialog.askstring("Zip file name dialog box",
                                                    "Enter your .zip file name here (without extension):")
    # Destroy memory object, release memory.
    content.quit()


def main() -> None:
    """Main logic workflow."""

    # Instantiating open and load file dialog window, choose file/files to process further.
    files_to_load = file_dialog()
    print("Selected files:", files_to_load)
    # Initiate start time.
    start_time = time.perf_counter()
    # Create get tkinter zip file object.
    content = Tk()

    states = StateManager(files_to_load)

    # Instantiate submit button variable via Button function from tkinter module.
    submitButton = Button(content,
                          text="Click to:\nSelect the OUTPUT DIRECTORY (where cropped files will be added).\nEnter the ZIP COMPRESSED FILE NAME (for zipping).",
                          command=partial(get_zip_file_name, content, states), padx=25, pady=25)
    # Configure visuals for dialog box.
    submitButton.pack()
    # Execute dialog box logic.
    content.mainloop()
    # Destroy object, release memory.
    content.destroy()

    if states.output_dir is None or states.output_zip_name is None:
        raise ValueError("Output dir and zip file name is required")
    if any(file_path.startswith(states.output_dir) for file_path in files_to_load):
        raise ValueError("One or more source files are in the output directory, overwriting has been prevented")

    # Instantiate empty processes list.
    processes: List[multiprocessing.Process] = []

    print("Output directory:", states.output_dir)
    print("Output zip filename:", states.output_zip_name)

    # WHEN YOU USE MULTIPROCESSING YOU MUST USE A POOL OTHERWISE THE MACHINE IS RISKING A CRASH WHEN IT CONSTANTLY PEEKS 100%
    process_pool = multiprocessing.Pool(processes=max(multiprocessing.cpu_count() - 2, 1))
    for file_path in files_to_load:
        # Create a single process, pass target function and arguments therein.
        process_pool.apply_async(crop_files, args=(file_path, states.output_dir))

    # Block pool of processes.
    process_pool.close()
    # Start execution of the current pool.
    process_pool.join()

    # Archiving all cropped videos inside Output folder.
    zip_directory(states.output_dir, states.output_zip_name)

    # Retrieve end time.
    end_time = time.perf_counter()

    # Print total workflow execution time - in seconds.
    print(f"Process completed. Execution time: {round(end_time - start_time, 2)} second(s).")
