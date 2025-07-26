import os


def get_files_info(working_directory: str, directory:str) -> str:
    working_path = os.path.abspath(working_directory)
    working_dir_contents = os.listdir(working_path)
    working_dir_contents.append(".")
    if directory not in working_dir_contents:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    path = os.path.join(working_path, directory)
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    dir_contents = os.listdir(path)
    if len(dir_contents) == 0:
        return f'Error: "{directory}" is empty'

    try:
        files_info: list[str] = []
        for entry in dir_contents:
            entry_path = os.path.join(path, entry)
            file_size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            files_info.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"