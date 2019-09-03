import re
import shutil
import Location
import os
from sexy_fun import (get_script_location,
                      cls)


def login():
    pc_dir = ''
    pattern = re.compile(r"({}\w+)+".format(os.path.sep))
    try:
        with open(os.path.join(get_script_location(), 'Pc_Playlist_Location.txt'), mode='r')as file:
            pc_dir = file.read()

        change = input(f"current Pc Playlist Location is:  {pc_dir}\n"
                       f"do you want to change it? [Y/n]")
        if change == 'Y':
            pc_dir = input('Drag and drop playlist folder from your PC:\n')
        match = pattern.search(pc_dir)
        pc_dir = match.group()
    except IOError:
        print(f"Pc Playlist location not set")
        pc_dir = input('Drag and drop playlist folder from your PC:\n')
    finally:
        with open(os.path.join(get_script_location(), 'Pc_Playlist_Location.txt'), mode='w')as file:
            file.write(pc_dir)
    cls()
    player_dir = input('Drag and drop playlist folder from your player:\n')

    match = pattern.search(player_dir)
    player_dir = match.group()

    return pc_dir, player_dir


def get_parent_directory(path: str):
    head, _ = os.path.split(path)
    return head


def get_relative_path(path: str, main_directory):
    try:
        return path[len(main_directory) + 1:]
    except TypeError:
        pass


def get_name(folder: str):
    _, tail = os.path.split(folder)
    return tail


def copy_folder(source_folder: Location, destination_folder: Location):
    shutil.copytree(source_folder.full_path, destination_folder.full_path)
    print(f"SYNCED {source_folder.relative_path}")


def copy_file(source_file, destination_folder):
    shutil.copy2(source_file,
                 destination_folder.full_path)

    print(f"SYNCED {get_name(source_file)}")


def remove_folder(destination_folder: Location):
    shutil.rmtree(destination_folder.full_path)
    print(f"REMOVED {destination_folder.relative_path}")


def remove_file(destination_file):
    os.remove(destination_file)
    print(f"REMOVED {get_name(destination_file)}")


def get_number_of_children(directory):
    directories = None
    for _, directories, _ in os.walk(directory):
        directories = directories
        break

    try:
        return len(directories)
    except TypeError:
        raise Exception(f'directory not found in {directory}\n')
