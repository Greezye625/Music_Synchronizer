from functions import get_path_relative_to_directory
import os


class Location:
    """

    """

    def __init__(self, full_path, path_relative_to_playlist_location):
        self.full_path = full_path
        self.path_relative_to_playlsit_location = path_relative_to_playlist_location
        # self.parent_directory = os.path.dirname(full_path)

    def get_parent(self):
        return os.path.dirname(self.full_path)
