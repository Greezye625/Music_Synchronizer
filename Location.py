from common_functions import (get_parent_directory,
                              get_relative_path)


class Location:
    """

    """

    def __init__(self, full_path, main_directory):
        self.full_path = full_path
        self.relative_path = get_relative_path(full_path, main_directory)
        self.parent_directory = get_parent_directory(full_path)
