import shutil
from Playlist import Playlist


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

    for folder in player_playlist.dirs_folders_list:
        if folder[1] in pc_folder_list:
            pass

        elif folder[1] not in pc_folder_list:
            print(f'we will delete{folder}')

            shutil.rmtree(folder)
            folder = 'clear'
        else:
            print('we have a problem bitch')

    player_playlist.dirs_folders_list = list(filter(lambda item: item != 'clear', player_playlist.dirs_folders_list))
