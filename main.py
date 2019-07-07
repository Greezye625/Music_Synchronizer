from get_folder_list import get_folder_list
import clean_player
from functions import *


def main():

    pc_dir = '/home/greezye/[.Greezye]/TEST/test1'
    player_dir = input('Drag and drop playlist folder from your player:\n')[1:-1]

    pc_header = create_headers(pc_dir)
    player_header = create_headers(player_dir)

    pc_folder_list = get_folder_list(pc_dir)
    player_folder_list = get_folder_list(player_dir)

    testx = pc_folder_list[2][len(pc_header):]
    print(testx)

    # clean_player.clean_folders(pc_folder_list, player_folder_list)


if __name__ == '__main__':
    main()
