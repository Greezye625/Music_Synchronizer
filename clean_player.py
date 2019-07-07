import shutil


def clean_folders(pc_folder_list=None, player_folder_list=None):
    """

    :param pc_folder_list:
    :param player_folder_list:
    :return:
    """

    if pc_folder_list is None:
        pc_folder_list = []

    if player_folder_list is None:
        player_folder_list =[]

    for folder in player_folder_list:
        if folder in pc_folder_list:
            pass
        elif folder not in pc_folder_list:
            shutil.rmtree(folder)

        else:
            print('we have a problem bitch')
