import os
import shutil
import Location


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
