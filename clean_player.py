from Playlist import Playlist
import os
from Location import Location
from common_functions import (get_parent_directory,
                              remove_file,
                              remove_folder,
                              get_number_of_children)


def delete_files_not_in_pc_playlist(player_folder: Location, pc_playlist: Playlist):
    """
    If twin folder is found on PC Playlist, Player folder contents are checked against
    the contents of PC folder, files existing on Player but not on PC are removed

    :param player_folder:
    :param pc_playlist:
    :return:
    """

    if None in (player_folder, pc_playlist):
        raise Exception('arg not delivered to delete_files_not_in_pc_playlist function in clean_player.py')

    pc_curr_folder_song_list = []

    # creating list of songs in PC twin of currently investigated Player folder
    for _, _, pc_files in os.walk(os.path.join(pc_playlist.directory, player_folder.relative_path)):
        for name in pc_files:
            pc_curr_folder_song_list.append(name)

    # checking and deleting file from currently investigated PLAYER folder,
    # if it's not in corresponding PC folder
    for root, _, files in os.walk(player_folder.full_path):
        for name in files:
            if name not in pc_curr_folder_song_list:
                remove_file(os.path.join(root, name))


def check_upper_folder(checked_folder: str, player_playlist: Playlist):
    """
    recursive func used to delete highest parent directory
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


    if folder that needed to be deleted was child_folder_3,
    then instead child_folder_1 would be deleted
    (with all it's children)
    :param player_playlist:
    :param checked_folder:
    :return:
    """

    parent = get_parent_directory(checked_folder)

    children_size = get_number_of_children(parent)

    if children_size == 1:
        check_upper_folder(checked_folder=parent,
                           player_playlist=player_playlist)
    elif children_size == 0:
        raise Exception(f'directories not found in {parent}')
    else:
        folder_to_delete = Location(full_path=checked_folder,
                                    main_directory=player_playlist.directory)
        remove_folder(folder_to_delete)


def delete_folders_not_in_pc_playlist(player_folder: Location, player_playlist: Playlist):
    """
    If twin folder is not found on PC Playlist, folder gets deleted from the Player.
    Addidtionally, check is performed to veryfy if deleted folder is the last one in it's parent
    directory. If it is, then the whole parent directory is removed.

    :param player_playlist:
    :param player_folder: tuple
    :return:
    """

    if player_folder is None:
        raise Exception('arg not delivered to delete_folders_not_in_pc_playlist function in clean_player.py')

    children_size = get_number_of_children(player_folder.parent_directory)

    """
    if parent of the folder has only one directory in it, then it's folder we're about to delete,
    so deleting Parent folder will achieve the same goal, and not leave empty parent folder.
    len(dirs) == 0 shouldn't ever happen, but left for safety
    """

    if children_size == 1:
        check_upper_folder(checked_folder=player_folder.parent_directory,
                           player_playlist=player_playlist)
    elif children_size == 0:
        raise Exception(f'directories not found in {player_folder.parent_directory}')
    else:
        remove_folder(player_folder)


def clean_player_folders(pc_playlist: Playlist, player_playlist: Playlist):
    """
    Function removes files and folders from player, that are non existent
    in playlist on PC

    :param pc_playlist:
    :param player_playlist:
    :return:
    """

    pc_folder_list = list(item.relative_path for item in pc_playlist.locations_list)

    for index, folder in enumerate(player_playlist.locations_list):

        if folder.relative_path in pc_folder_list:  # if folder from PLAYER is in playlist on PC
            delete_files_not_in_pc_playlist(player_folder=folder,
                                            pc_playlist=pc_playlist)

        else:
            delete_folders_not_in_pc_playlist(player_folder=folder,
                                              player_playlist=player_playlist)
            player_playlist.locations_list[index] = 'clear'  # marking folder for removal

    # filtering out folders marked for removal and saving to dirs_folders_parents_list
    player_playlist.locations_list = list(
            filter(lambda item: item != 'clear', player_playlist.locations_list))
