import shutil


def clean_player_folders(pc_dir, player_dir, pc_folder_list=None, player_folder_list=None):
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
        if folder[len(player_dir)] in map(lambda item: item[len(pc_dir)], pc_folder_list):
            pass

        elif folder[len(player_dir)] not in map(lambda item: item[len(pc_dir)], pc_folder_list):
            print(f'we will delete{folder}')

            shutil.rmtree(folder)
        else:
            print('we have a problem bitch')
