import shutil
from Playlist import Playlist
import os


def delete_files_not_in_pc_playlist(folder: tuple, pc_playlist: Playlist, pc_curr_folder_song_list: list):
    """
    If twin folder is found on PC Playlist, Player folder contents are checked against
    the contents of PC folder, files existing on Player but not on PC are removed

    :param folder:
    :param pc_playlist:
    :param pc_curr_folder_song_list:
    :return:
    """
    if None in (folder, pc_playlist, pc_curr_folder_song_list):
        raise Exception('arg not delivered to delete_files_not_in_pc_playlist function in clean_player.py')

    # creating list of songs in PC twin of currently investigated Player folder
    for pc_root, pc_dirs, pc_files in os.walk(pc_playlist.directory + folder[1]):
        for name in pc_files:
            pc_curr_folder_song_list.append(name)

    # checking and deleting file from currently investigated PLAYER folder,
    # if it's not in corresponding PC folder
    for root, _, files in os.walk(folder[0]):
        for name in files:
            if name not in pc_curr_folder_song_list:
                os.remove(os.path.join(root, name))


def delete_folders_not_in_pc_playlist(folder: tuple):
    """
    If twin folder is not found on PC Playlist, folder gets deleted from the Player.
    Addidtionally, check is performed to veryfy if deleted folder is the last one in it's parent
    directory. If it is, then the whole parent directory is removed.

    :param folder: tup
    :return:
    """
    def check_upper_folder(parent: str):
        """
        recursive func to check folders up the directory tree, used to delete highest parent directory
        instead of child directory, if child directory is the only content.

        e.g

        parent_folder
              |
              |--child_folder_1
              |       |
              |       |--child_folder_2
              |               |
              |               |--child_folder_3
              |
              |--child_folder_4


        if folder that needed to be deleted was child_folder_3, then instead child_folder_1 would be deleted
        (with all it's children)
        :param parent:
        :return:
        """

        upper_folder = '/'.join(parent.split('/')[:-1])

        directories = None
        for _, directories, _ in os.walk(upper_folder):
            directories = directories
            break

        if directories is None:
            raise Exception(f'directory not found in {upper_folder}\n')

        if len(directories) == 1:
            check_upper_folder(upper_folder)
        elif len(directories) == 0:
            raise Exception(f'directories not found in {upper_folder}')
        else:
            shutil.rmtree(parent)

    if folder is None:
        raise Exception('arg not delivered to delete_folders_not_in_pc_playlist function in clean_player.py')

    dirs = None
    for _, dirs, _ in os.walk(folder[2]):
        dirs = dirs
        break

    if dirs is None:
        raise Exception(f'directory not found in {folder[2]}')

    """
    if parent of the folder has only one directory in it, then it's folder we're about to delete,
    so deleting Parent folder will achieve the same goal, and not leave empty parent folder.
    len(dirs) == 0 shouldn't ever happen, but left for safety
    """
    if len(dirs) == 1:
        check_upper_folder(folder[2])
    elif len(dirs) == 0:
        raise Exception(f'directories not found in {folder[2]}')
    else:
        shutil.rmtree(folder[0])  # removing just the investigated PLAYER folder


def clean_player_folders(pc_playlist=None, player_playlist=None):
    """
    Function removes files and folders from player, that are non existent
    in playlist on PC

    :param pc_playlist:
    :param player_playlist:
    :return:
    """

    if pc_playlist is None:
        pc_playlist = Playlist()

    if player_playlist is None:
        player_playlist = Playlist()

    # unziping dirs_folders_parents_list into seperate lists for every data
    pc_dir_list, pc_folder_list, pc_parent_list = zip(*pc_playlist.dirs_folders_parents_list)
    pc_dir_list, pc_folder_list, pc_parent_list = list(pc_dir_list), list(pc_folder_list), list(pc_parent_list)

    pc_curr_folder_song_list = []  # list containing names of files in folder currently looked into

    """
    in dirs_folders_parents_list:
    folder[0] = whole directory of current folder
    folder[1] = folder direcotry excluding directory of the playlist
                corresponding folders in the PC and PLAYER Playlists will have this value identical
    folder[2] = Parent folder of the current folder
    """
    for index, folder in enumerate(player_playlist.dirs_folders_parents_list):

        if folder[1] in pc_folder_list:                     # if folder from PLAYER is in playlist on PC
            delete_files_not_in_pc_playlist(folder=folder,
                                            pc_playlist=pc_playlist,
                                            pc_curr_folder_song_list=pc_curr_folder_song_list)

        else:           # if folder from PLAYER is not in playlist on PC
            delete_folders_not_in_pc_playlist(folder)
            player_playlist.dirs_folders_parents_list[index] = 'clear'  # marking folder for removal

    # filtering out folders marked for removal and saving to dirs_folders_parents_list
    player_playlist.dirs_folders_parents_list = list(
        filter(lambda item: item != 'clear', player_playlist.dirs_folders_parents_list))
