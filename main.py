from clean_player import *
from Playlist import Playlist
from sexy_fun import *


def main():
    # pc_dir = input('Drag and drop playlist folder from your PC:\n')
    # player_dir = input('Drag and drop playlist folder from your player:\n')

    # Mac directories
    pc_dir = '/Users/jsobi/Python/Music_Synchronizer/Disk1/Playlist'
    player_dir = '/Users/jsobi/Python/Music_Synchronizer/Disk2/Playlist'

    # Linux directories
    # pc_dir = '/home/greezye/Greezye/TEST/Disk1/Playlist'
    # player_dir = '/home/greezye/Greezye/TEST/Disk2/Playlist'

    pc_playlist = Playlist(pc_dir)

    player_playlist = Playlist(player_dir)

    clean_player_folders(pc_playlist, player_playlist)


    # testx = pc_folder_list[3][len(pc_dir):]
    # print(testx)
    #
    # testy = player_folder_list[3][len(player_dir):]
    # print(testy)
    #
    # clean_player_folders(pc_dir, player_dir, pc_folder_list, player_folder_list)


if __name__ == '__main__':
    main()
