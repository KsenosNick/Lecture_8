
import os

directory_name = 'task_8.3_files'
file_path = os.path.join(os.getcwd(), directory_name)


def get_file_list(path):
    file_list = []
    new_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(file)
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            str_list = file.readlines()
            str_list = [line.rstrip('\n') for line in str_list]
            new_dict[file_name] = str_list
            file.close()
        new_dict = {file_name: str_list for file_name, str_list in
                    sorted(new_dict.items(), key=lambda strings: len(strings[1]))}

    return new_dict


def write_file(dictionary, path):
    os.walk(path)
    file = open(f'{path}/file.txt', 'w', encoding="utf-8")
    for key, value in dictionary.items():
        file.write(f'{key}\n{len(value)}\n')
        for strings in value:
            file.write(f'{strings}\n')


new_file = get_file_list(file_path)

write_file(new_file, directory_name)
