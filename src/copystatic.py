import os
import shutil

def clear_public(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def copy_static(path1, path2):
    for item in os.listdir(path1):
        path_of_file = os.path.join(path1, item)
        second_path = os.path.join(path2, item)
        if os.path.isfile(path_of_file):
            shutil.copy(path_of_file, second_path)
        else:
            os.mkdir(second_path)
            copy_static(path_of_file, second_path)
