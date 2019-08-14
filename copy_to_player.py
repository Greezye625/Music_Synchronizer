import shutil
from Playlist import Playlist
import os

def copy_folders_not_on_player():
    pass


def copy_files_not_on_player():
    pass


def copy_music_to_player(pc_playlist=None, player_playlist=None):
    if pc_playlist is None:
        pc_playlist=Playlist()
    if player_playlist is None:
        player_playlist = Playlist()

