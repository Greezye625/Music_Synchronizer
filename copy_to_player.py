import shutil
from Playlist import Playlist
import os


def copy_folders_not_on_player(folder: tuple, pc_playlist=None, player_playlist=None):

    def check_up_for_non_existent_folder(parent):
        next_parent = '/'.join(parent.split('/')[:-1])
        if os.path.isdir(os.path.join(player_playlist.directory, next_parent)):
            shutil.copytree(os.path.join(pc_playlist.directory, parent),
                            os.path.join(player_playlist.directory, parent))
        else:
            check_up_for_non_existent_folder(next_parent)

    if pc_playlist is None:
        pc_playlist = Playlist()
    if player_playlist is None:
        player_playlist = Playlist()

    relative_parent = '/'.join(folder[1].split('/')[:-1])

    if os.path.isdir(os.path.join(player_playlist.directory, relative_parent)):
        shutil.copytree(folder[0], os.path.join(pc_playlist.directory, relative_parent))
    else:
        check_up_for_non_existent_folder(relative_parent)


def copy_files_not_on_player(folder: tuple, player_playlist: Playlist):
    player_curr_folder_song_list = []       # list containing names of files in folder currently looked into

    # creating list of songs in Player twin of currently investigated PC folder
    for _, _, player_files in os.walk(player_playlist.directory + folder[1]):
        for name in player_files:
            player_curr_folder_song_list.append(name)

    for root, _, files in os.walk(folder[0]):
        for name in files:
            if name not in player_curr_folder_song_list:
                shutil.copy2(os.path.join(root, name),
                             os.path.join(player_playlist.directory, folder[1]))


def copy_music_to_player(pc_playlist=None, player_playlist=None):
    if pc_playlist is None:
        pc_playlist = Playlist()
    if player_playlist is None:
        player_playlist = Playlist()

    _, player_folder_list, _ = zip(*player_playlist.dirs_folders_parents_list)
    _, player_folder_list, _ = list(player_folder_list)

    for index, folder in enumerate(pc_playlist.dirs_folders_parents_list):

        # currently investigated folder is in player playlist
        if folder[1] in player_folder_list:
            copy_files_not_on_player(folder=folder,
                                     player_playlist=player_playlist)

        # currently investigated folder not in player playlist
        elif folder[1] not in player_folder_list:
            if not os.path.isdir(os.path.join(player_playlist.directory, folder[1])):
                copy_folders_not_on_player(folder)
