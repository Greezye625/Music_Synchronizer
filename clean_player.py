import shutil
from Playlist import Playlist
import os


def clean_player_folders(player_playlist=None, pc_playlist=None):
    """

    :param player_playlist:
    :param pc_playlist:
    :return:
    """

    if pc_playlist is None:
        pc_playlist = Playlist()

    if player_playlist is None:
        player_playlist = Playlist()

    pc_dir_list, pc_folder_list = zip(*pc_playlist.dirs_folders_list)
    pc_dir_list, pc_folder_list = list(pc_dir_list), list(pc_folder_list)

    pc_curr_folder_song_list = []

    for folder in player_playlist.dirs_folders_list:
        if folder[1] in pc_folder_list:

            for pc_root, pc_dirs, pc_files in os.walk("".join(pc_playlist.directory, folder[1])):
                for name in pc_files:
                    pc_curr_folder_song_list.append(name)

            for root, _, files in os.walk(folder[0]):  # searching tree with root in 'folder[0]'
                for name in files:
                    if name in pc_curr_folder_song_list:
                        shutil.rmtree(os.path.join(root, name))

        elif folder[1] not in pc_folder_list:
            shutil.rmtree(folder)
            folder = 'clear'
        else:
            print('we have a problem bitch')

    player_playlist.dirs_folders_list = list(filter(lambda item: item != 'clear', player_playlist.dirs_folders_list))
