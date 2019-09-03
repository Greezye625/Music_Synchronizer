from Playlist import Playlist
import os
from Location import Location
from functions import (get_parent_directory,
                       copy_folder,
                       copy_file)


def check_tree_up_for_non_existent_folder(pc_playlist: Playlist, player_playlist: Playlist, checked_folder: str):
    """
    recursive func, used to find first non existent directory going up the tree.
    to copy content into it

    e.g
    folders needed to sync to Player are:
    artist/album1/CD1
    artist/album1/CD2

    but 'album1' doesn't exist in 'artist' folder on Player, then this func will copy
    'album1' and all it's children to 'artist'

    :param player_playlist:
    :param pc_playlist:
    :param checked_folder:
    :return:
    """

    parent = get_parent_directory(checked_folder)

    # if parent exist -> copying folders into parent
    if os.path.isdir(os.path.join(player_playlist.directory, parent)):

        pc_folder = Location(full_path=os.path.join(pc_playlist.directory, checked_folder),
                             main_directory=pc_playlist.directory)
        player_folder = Location(full_path=os.path.join(player_playlist.directory, checked_folder),
                                 main_directory=player_playlist.directory)

        copy_folder(source_folder=pc_folder,
                    destination_folder=player_folder)

    # if parent doesn't exist -> checking it's parent to see if it exist
    else:
        check_tree_up_for_non_existent_folder(pc_playlist=pc_playlist,
                                              player_playlist=player_playlist,
                                              checked_folder=parent)


def copy_folders_not_on_player(pc_folder: Location, pc_playlist: Playlist, player_playlist: Playlist):
    """
    copying folders from PC to Player, before copying a folder function checks folder structure for non existent parents

    e.g.
    wnen copying album, fucntion checks if artist folder exist, and if not copies artist folder with all subfolders

    :param pc_folder:
    :param pc_playlist:
    :param player_playlist:
    :return:
    """

    relative_parent = get_parent_directory(pc_folder.relative_path)

    # if parent of checked folder exists on player -> copying files into it
    if os.path.isdir(os.path.join(player_playlist.directory, relative_parent)):

        player_folder = Location(full_path=os.path.join(player_playlist.directory, pc_folder.relative_path),
                                 main_directory=player_playlist.directory)

        copy_folder(source_folder=pc_folder,
                    destination_folder=player_folder)

    # if parent of checked folder doesn't exists on player -> checking if it's parent exists
    else:
        check_tree_up_for_non_existent_folder(pc_playlist=pc_playlist,
                                              player_playlist=player_playlist,
                                              checked_folder=relative_parent)


def copy_files_not_on_player(pc_folder: Location, player_playlist: Playlist):
    """
    function copying songs from PC to Player Playlist
    (in scope of currently investigated folder)

    :param pc_folder: Location
    :param player_playlist: Playlist
    :return:
    """

    player_curr_folder_song_list = []

    # creating list of songs in Player twin of currently investigated PC Playlist folder
    for _, _, player_files in os.walk(os.path.join(player_playlist.directory, pc_folder.relative_path)):
        for name in player_files:
            player_curr_folder_song_list.append(name)

    # copying music files to album folder on Player
    for root, _, files in os.walk(pc_folder.full_path):
        for name in files:
            if name not in player_curr_folder_song_list:
                player_folder = Location(full_path=os.path.join(player_playlist.directory,
                                                                pc_folder.relative_path),
                                         main_directory=player_playlist.directory)

                copy_file(source_file=os.path.join(root, name),
                          destination_folder=player_folder)


def copy_music_to_player(pc_playlist: Playlist, player_playlist: Playlist):
    """
    function copying folders and files to Player Playlist

    :param pc_playlist:
    :param player_playlist:
    :return:
    """

    # list of relative paths of folders in player playlist
    player_folder_list = list(item.relative_path for item in player_playlist.locations_list)

    for index, folder in enumerate(pc_playlist.locations_list):

        # currently investigated folder is in player playlist
        if folder.relative_path in player_folder_list:
            copy_files_not_on_player(pc_folder=folder,
                                     player_playlist=player_playlist)

        # currently investigated folder not in player playlist
        elif folder.relative_path not in player_folder_list:
            if not os.path.isdir(os.path.join(player_playlist.directory, folder.relative_path)):
                copy_folders_not_on_player(pc_folder=folder,
                                           pc_playlist=pc_playlist,
                                           player_playlist=player_playlist)
