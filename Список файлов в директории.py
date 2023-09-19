import os

def get_file_list(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

directory = "./hourly_data"  # Укажите путь к нужной директории

files = get_file_list(directory)
for file in files:
    print(file)