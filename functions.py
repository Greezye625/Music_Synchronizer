def create_headers(directory=None):
    """
    Creates "headers" from playlist directories
    header is a directory preceeding playlist folder.
    They're needed to compare playlist folders directories
    with different beginnings.

    With 2 files/folders which have the same place in the playlist,
    slicing both of them with =>[len(header):] gives identical strings

    pc_dir[len(pc_header)] == player_dir[len(player_dir)]

    :param directory:
    :return:
    """
    directory_split = directory[1:].split('/')               # splitting directories strings into lists of folder names

    header = ''

    for item in directory_split:                     #
        header += f'/{item}'                         # Creating headers by appending folder names until reaching
        if item == 'test1':                          # playlist name
            break                                    #

    return header
