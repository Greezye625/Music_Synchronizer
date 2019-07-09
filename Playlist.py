import os


class Playlist:
    def __init__(self, directory='', dirs_folders_list=None):
        if dirs_folders_list is None:
            dirs_folders_list = []

        self.directory = directory
        self.dirs_folders_list = dirs_folders_list

    def get_folder_list(self):
        """
        Creates lists of folders by tree search from root specified by directory
        then sorts it and filters to leave only leaves from the tree,
        just the lowest children folders with audio files.

        :return:
        """

        for root, dirs, files in os.walk(self.directory):                    # searching tree with root in 'directory'
            for name in dirs:                                           # creating list of folders and subfolders
                self.dirs_folders_list.append(os.path.join(root, name))           #

        self.dirs_folders_list.sort()                                              # when list of folders is sorted, parent directories
                                                                        # can be discovered and deleted by checking if next
        for index in range(len(self.dirs_folders_list) - 1):                       # position on the list contains the entirety of
            if self.dirs_folders_list[index + 1].startswith(self.dirs_folders_list[index]):   # current position. Then marking parrent directory
                self.dirs_folders_list[index] = 'clear'                            # for deletion

        self.dirs_folders_list = list((filter(lambda element: element != 'clear', self.dirs_folders_list)))   # erasing marked positions

        names_list = (item[len(self.directory):] for item in self.dirs_folders_list)

        self.dirs_folders_list = list(zip(self.dirs_folders_list, names_list))

        print()
