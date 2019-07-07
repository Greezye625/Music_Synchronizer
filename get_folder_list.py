import os


def get_folder_list(directory):
    """
    Creates lists of folders by tree search from root specified by directory
    then sorts it and filters to leave only leaves from the tree,
    just the lowest children folders with audio files.

    :param directory:
    :return:
    """

    folder_list = []

    for root, dirs, files in os.walk(directory):                    # searching tree with root in 'directory'
        for name in dirs:                                           # creating list of folders and subfolders
            folder_list.append(os.path.join(root, name))            #

    folder_list.sort()                                              # when list of folders is sorted, parent directories
                                                                    # can be discovered and deleted by checking if next
    for index in range(len(folder_list) - 1):                       # position on the list contains the entirety of
        if folder_list[index + 1].startswith(folder_list[index]):   # current position. Then marking parrent directory
            folder_list[index] = 'clear'                            # for deletion

    folder_list = list((filter(lambda element: element != 'clear', folder_list)))   # erasing marked positions

    return folder_list
