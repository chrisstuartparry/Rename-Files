import re
import os
import tkinter as tk
from tkinter import filedialog


def remove_number_in_parentheses(filename):
    # Use a regular expression to remove parentheses with numbers inside them
    new_filename = re.sub(r"\(\d+\)", "", filename)
    return new_filename


def main():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()

    print("Choose a folder containing the files or the files themselves.")

    # Open a folder selector window
    # input_directory = filedialog.askdirectory(title="Select a folder")

    # If you want to allow users to select multiple files instead of a folder, uncomment the following line
    input_files = filedialog.askopenfilenames(
        title="Select files", filetypes=[("PDF files", "*.pdf")]
    )

    # for filename in os.listdir(input_directory):
    #     if filename.endswith(".pdf"):
    #         new_filename = remove_number_in_parentheses(filename)
    #         input_file_path = os.path.join(input_directory, filename)
    #         output_file_path = os.path.join(input_directory, new_filename)

    #         os.rename(input_file_path, output_file_path)

    # If you allowed users to select multiple files, use the following loop instead
    for input_file_path in input_files:
        filename = os.path.basename(input_file_path)
        if filename.endswith(".pdf"):
            new_filename = remove_number_in_parentheses(filename)
            output_file_path = os.path.join(
                os.path.dirname(input_file_path), new_filename
            )
            os.rename(input_file_path, output_file_path)


if __name__ == "__main__":
    main()
