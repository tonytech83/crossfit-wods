import os
from datetime import datetime

data_dir = 'data'

def format_date_from_filename(filename):
    date_part = filename.split('.')[0]  # "2022-06-21"
    date_obj = datetime.strptime(date_part, "%Y-%m-%d")

    return date_obj.strftime("%d %B %Y")

def get_data_dir():
    """
    Create a list of dictionaries with file name and formatted date from the file name.
    Reassigns indices after sorting by date.
    :return: List of dictionaries sorted by date.
    """
    # Extract filenames and dates
    data_files = [
        {"filename": file, "formatted_date": format_date_from_filename(file)}
        for file in os.listdir(data_dir)
        if file.endswith('.html')
    ]

    # Sort by date derived from the filename
    data_files.sort(key=lambda x: datetime.strptime(x["filename"].split('.')[0], "%Y-%m-%d"))

    # Reassign idx after sorting
    for idx, item in enumerate(data_files):
        item["idx"] = idx

    return data_files


def prepare_file_content(filename):
    file_path = os.path.join(data_dir, filename)

    if not os.path.exists(file_path):
        return "File not found", 404

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return content
