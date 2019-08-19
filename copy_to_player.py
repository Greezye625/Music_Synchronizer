import shutil
from Playlist import Playlist
import os
from Location import Location


def copy_folders_not_on_player(folder: Location, pc_playlist: Playlist, player_playlist: Playlist):

    def check_up_for_non_existent_folder(parent):
        next_parent = '/'.join(parent.split('/')[:-1])
        if os.path.isdir(os.path.join(player_playlist.directory, next_parent)):
            shutil.copytree(os.path.join(pc_playlist.directory, parent),
                            os.path.join(player_playlist.directory, parent))
        else:
            check_up_for_non_existent_folder(next_parent)

    relative_parent = '/'.join(folder.relative_path.split('/')[:-1])

    test = os.path.join(player_playlist.directory, relative_parent)

    if os.path.isdir(os.path.join(player_playlist.directory, relative_parent)):
        new_folder_name = folder.relative_path[len(relative_parent)+1:]
        shutil.copytree(folder.full_path, os.path.join(player_playlist.directory, folder.relative_path))
    else:
        check_up_for_non_existent_folder(relative_parent)


def copy_files_not_on_player(folder: Location, player_playlist: Playlist):
    player_curr_folder_song_list = []       # list containing names of files in folder currently looked into

    # creating list of songs in Player twin of currently investigated PC folder
    for _, _, player_files in os.walk(os.path.join(player_playlist.directory, folder.relative_path)):
        for name in player_files:
            player_curr_folder_song_list.append(name)

    for root, _, files in os.walk(folder.full_path):
        for name in files:
            if name not in player_curr_folder_song_list:
                shutil.copy2(os.path.join(root, name),
                             os.path.join(player_playlist.directory, folder.relative_path))


def copy_music_to_player(pc_playlist: Playlist, player_playlist: Playlist):

    player_folder_list = list(item.relative_path for item in player_playlist.locations_list)

    for index, folder in enumerate(pc_playlist.locations_list):

        # currently investigated folder is in player playlist
        if folder.relative_path in player_folder_list:
            copy_files_not_on_player(folder=folder,
                                     player_playlist=player_playlist)

        # currently investigated folder not in player playlist
        elif folder.relative_path not in player_folder_list:
            if not os.path.isdir(os.path.join(player_playlist.directory, folder.relative_path)):
                copy_folders_not_on_player(folder=folder,
                                           pc_playlist=pc_playlist,
                                           player_playlist=player_playlist)
