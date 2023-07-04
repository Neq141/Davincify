import os
from moviepy.editor import *

def convert_to_mov(input_file, output_mov):
    """
    Converts a video file to MOV format.

    Args:
        input_file (str): Path to the input video file.
        output_mov (str): Path to the output MOV file.

    Returns:
        None
    """
    video = VideoFileClip(input_file)
    video.write_videofile(output_mov, codec='png')

def convert_videos_in_directory(input_dir, output_dir):
    """
    Crawls a given directory, creates new directories for each input folder, copies the directory structure to
    the output folder, and converts video files inside each folder to MOV format.

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.

    Returns:
        None
    """
    for root, dirs, files in os.walk(input_dir):
        # Create the corresponding directory structure in the output folder
        relative_path = os.path.relpath(root, input_dir)
        output_path = os.path.join(output_dir, relative_path)
        os.makedirs(output_path, exist_ok=True)

        for filename in files:
            if filename.lower().endswith(('.mp4', '.avi', '.mkv')):
                input_file = os.path.join(root, filename)
                output_file = os.path.join(output_path, f"{os.path.splitext(filename)[0]}.mov")
                convert_to_mov(input_file, output_file)

def main():
    """
    Main function that converts video files in the specified directory to MOV format, while preserving the directory structure.
    """
    input_directory = input("please enter the directory that you want to davincify\n\n|->")  # Replace with your input directory path
    output_directory = f"davincify-{input_directory}"  # Replace with your output directory path

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    convert_videos_in_directory(input_directory, output_directory)
    print("done")

if __name__ == "__main__":
    main()
