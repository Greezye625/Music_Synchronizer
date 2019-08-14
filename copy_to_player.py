import shutil
from Playlist import Playlist
import os


def copy_folders_not_on_player(folder: tuple, pc_playlist=None, player_playlist=None):
    if pc_playlist is None:
        pc_playlist = Playlist()
    if player_playlist is None:
        player_playlist = Playlist()

    shutil.copytree(folder[0], os.path.join(player_playlist.directory, folder[1]))


def copy_files_not_on_player():
    pass


def copy_music_to_player(pc_playlist=None, player_playlist=None):
    if pc_playlist is None:
        pc_playlist = Playlist()
    if player_playlist is None:
        player_playlist = Playlist()

    player_dir_list, player_folder_list, player_parent_list = zip(*player_playlist.dirs_folders_parents_list)
    player_dir_list, player_folder_list, player_parent_list = list(player_dir_list), list(player_folder_list), list(player_parent_list)

    player_curr_folder_song_list = []  # list containing names of files in folder currently looked into

    for index, folder in enumerate(pc_playlist.dirs_folders_parents_list):

        # currently investigated folder is in player playlist
        if folder[1] in player_folder_list:
            pass

        # currently investigated folder not in player playlist
        elif folder[1] not in player_folder_list:
            copy_folders_not_on_player(folder)
