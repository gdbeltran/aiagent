import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(os.path.join(working_directory, directory))
    if os.path.commonpath([abs_working_directory, abs_full_path]) != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    if directory == ".":
        result = ["Result for current directory:"]
    else:
        result = [f"Result for '{directory}' directory:"]
    contents = os.listdir(abs_full_path)
    for item in contents:
        item_path = os.path.join(abs_full_path, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        result.append(f" - {item}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(result)
        