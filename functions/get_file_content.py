import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonpath([abs_working_directory, abs_full_path]) != abs_working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(abs_full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if os.path.getsize(abs_full_path) > MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string