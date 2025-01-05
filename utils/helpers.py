import os

data_dir = 'data'

def get_data_dir():

    data_files = [file for file in os.listdir(data_dir) if file.endswith('.html')]

    return data_files

def prepare_file_content(filename):
    file_path = os.path.join(data_dir, filename)

    if not os.path.exists(file_path):
        return "File not found", 404

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return content
