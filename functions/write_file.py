import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonpath([abs_working_directory, abs_full_path]) != abs_working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    dir_name = os.path.dirname(abs_full_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(abs_full_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'