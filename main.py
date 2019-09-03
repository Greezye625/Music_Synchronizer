from clean_player import *
from copy_to_player import *
from Playlist import Playlist
from functions import login
from sexy_fun import cls


def main():
    # Mac directories
    # pc_dir = '/Users/jsobi/Python/Music_Synchronizer/Disk1/Playlist'
    # player_dir = '/Users/jsobi/Python/Music_Synchronizer/Disk2/Playlist'

    # Linux directories
    pc_dir = '/home/greezye/Greezye/TEST/Disk1/Playlist'
    player_dir = '/home/greezye/Greezye/TEST/Disk2/Playlist'

    pc_dir, player_dir = login()
    cls()

    pc_playlist = Playlist(pc_dir)

    player_playlist = Playlist(player_dir)

    print("----------------CLEANING PLAYLIST----------------")

    clean_player_folders(pc_playlist, player_playlist)

    cls()

    print("----------------SYNCING PLAYLIST----------------")

    copy_music_to_player(pc_playlist=pc_playlist,
                         player_playlist=player_playlist)

    cls()


if __name__ == '__main__':
    main()
