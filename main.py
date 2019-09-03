from clean_player import *
from copy_to_player import *
from Playlist import Playlist
from functions import login
from sexy_fun import cls


def main():
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
