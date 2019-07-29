import os


class Playlist:
    def __init__(self, directory='', dirs_folders_list=None):
        if dirs_folders_list is None:
            dirs_folders_list = []

        self.directory = directory
        self.dirs_folders_parents_list = dirs_folders_list

        self.get_folder_list()

    def get_folder_list(self):
        """
        Creates lists of folders by tree search from root specified by directory
        then sorts it and filters to leave only leaves from the tree,
        just the lowest children folders with audio files.

        :return:
        """

        for root, dirs, files in os.walk(self.directory):  # searching tree with root in 'directory'
            for name in dirs:  # creating list of folders and subfolders
                self.dirs_folders_parents_list.append(os.path.join(root, name))  #

        self.dirs_folders_parents_list.sort()

        # when list of folders is sorted, parent directories
        # can be discovered and deleted by checking if next
        # position on the list contains the entirety of
        # current position. Then marking parent directory
        # for deletion
        for index in range(len(self.dirs_folders_parents_list) - 1):
            if self.dirs_folders_parents_list[index + 1].startswith(self.dirs_folders_parents_list[index]):
                self.dirs_folders_parents_list[index] = 'clear'

        self.dirs_folders_parents_list = list(
            (filter(lambda element: element != 'clear', self.dirs_folders_parents_list)))  # erasing marked positions

        # creating list of folder names excluding playlist location
        # e.g. /home/user/playlist/artist/album_xyz will result in name "/artist/album_xyz"
        names_list = (item[len(self.directory):] for item in self.dirs_folders_parents_list)

        # creating list of parent directories for every position
        parents_list = ('/'.join(item.split('/')[:-1]) for item in self.dirs_folders_parents_list)

        # zipping together to create list of tuples (directory,name, parent)
        self.dirs_folders_parents_list = list(zip(self.dirs_folders_parents_list, names_list, parents_list))
