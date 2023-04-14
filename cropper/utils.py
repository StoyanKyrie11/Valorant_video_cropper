from typing import List
import os
import zipfile


def retrieve_file_names(dirName: str) -> List[str]:
    """Function to designed to return all video .mp4 files in Output folder within project parent folder."""

    # Instantiate emtpy file paths list.
    filePaths = []
    # Loop - Read root, directory, subdirectories and file lists.
    for _, _, files in os.walk(dirName):
        for filename in files:
            # Appending all file path values with extension in respective list.
            filePaths.append(dirName + "/" + filename)

    # Return all relative file paths.
    return filePaths


def zip_directory(output_dir: str, zip_file_name: str) -> None:
    """Function to retrieve all video files, create ZipFile context manager, add all files to zip, save ZipFile."""

    # Create extension name.
    zip_file_ext = ".zip"

    # Call the function to retrieve all file names within the assigned Output folder.
    file_names = retrieve_file_names(output_dir)
    # Writing files via zipfile context manager.
    with zipfile.ZipFile(f'{zip_file_name}{zip_file_ext}', 'w') as zip_obj:
        # Inserting each file in .zip one by one.
        for file in file_names:
            zip_obj.write(file)
