import os
from Location import Location
from functions import get_path_relative_to_directory


class Playlist:
    """
    Class Containing information about Playlist.
    """

    def __init__(self, directory=''):
        self.directory = directory
        self.locations_list = []

        self.get_folder_list()

    def get_folder_list(self):
        """
        Creates lists of folders by tree search from root specified by directory
        then sorts it and filters to leave only leaves from the tree,
        just the lowest children folders with audio files.

        :return:
        """

        for root, dirs, files in os.walk(self.directory):  # searching tree with root in 'directory'
            for name in dirs:                              # creating list of folders and subfolders
                self.locations_list.append(os.path.join(root, name))

        self.locations_list.sort()

        """
        when list of folders is sorted, parent directories
        can be discovered and deleted by checking if next
        position on the list contains the entirety of
        current position. Then marking parent directory
        for deletion
        """
        for index in range(len(self.locations_list) - 1):
            if self.locations_list[index + 1].startswith(self.locations_list[index]):
                self.locations_list[index] = 'clear'

        # erasing marked positions
        self.locations_list = list((filter(lambda element: element != 'clear', self.locations_list)))

        self.locations_list = list(Location(full_path=item,
                                            path_relative_to_playlist_location=get_path_relative_to_directory(item, self.directory)) for item in self.locations_list)
