import os

MAX_CHARS = 10_000


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_path = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_path, file_path))

        if not full_path.startswith(working_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, 'r') as f:
            file_contents = f.read(MAX_CHARS)

        if len(file_contents) == 10_000:
            file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_contents
    except Exception as e:
        return f"Error: {e}"