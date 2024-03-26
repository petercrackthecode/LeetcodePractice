# https://leetcode.com/problems/design-file-system
from collections import defaultdict
from typing import Dict, Optional


class FileSystem:

    def __init__(
        self,
        dirname: str = "",
        val: int = 0,
        children: Dict[str, Optional["FileSystem"]] = defaultdict(lambda: None),
    ):
        """
        "/a",1

        '/a/b/c'

        'a/b/d'


        a
        - b - c
            - d

        a/c/d
        """
        self.dirname: str = dirname
        self.val: int = val
        self.children: Dict[str, Optional["FileSystem"]] = children

    def createPath(self, path: str, value: int) -> bool:
        """
        - if the path already exists or its parent path doesn't exist: return False
        - otherwise:
            -create a new path & associate value to path
            - return True

        "/a",1

        '/a/b/c'

        'a/b/d'


        a
        - b - c
            - d

        a/c/d
        always write pseudo code
        - if path == '' or '/': return False
        - split path into folders
        - have a variable called temp to loop thru our FileSystem: temp = self
        - loop: for each folder at index i in folder:
            - if folder in temp.children:
                - if i == len(folders) - 1 => the folder already exists: return False
                - otherwise: temp = temp.children[folder]
            - otherwise (folder is not in temp):
                - if i != len(folders) - 1 (not the last index => parent folder):
                    - return False
        - passed all the tests => create the folder:
        - temp.children[folder] = FileSystem
        """
        if path in {"", "/"}:
            return False
        folders = [folder for folder in path.split("/") if folder != ""]
        # print(f'folders = {folders}')
        temp: "FileSystem" = self
        # check if the paths already exists
        for i, folder in enumerate(folders):
            # print(f'folder = {folder}')
            # print(f'i = {i}\n')
            if folder in temp.children:
                if i == len(folders) - 1:
                    return False
                temp = temp.children[folder]
            else:  # folder doesn't exist in temp.children
                if i != len(folders) - 1:
                    return False

        new_folder = folders[-1]
        temp.children[new_folder] = FileSystem(new_folder, value, defaultdict(lambda: None))

        # print('------')
        return True

    def get(self, path: str) -> int:
        """
        - if the path doesn't exist: return -1
        - otherwise, returns the value at `path`

        - if path == '' or '/': return False
        - split the path into: folders
        - have a variable called temp to loop thru our FileSystem. temp:"FileSystem" = self

        - loop: for each folder at index i in folder:
            - if folder doesn't exist in temp.children:
                return False
            - otherwise: # folder exists in temp
                - temp = temp.children[folder]
        - ans = temp.val
        - return ans
        """
        if path in {"", "/"}:
            return False

        folders = [folder for folder in path.split("/") if folder != ""]
        temp: "FileSystem" = self

        for i, folder in enumerate(folders):
            if folder not in temp.children:
                return -1

            temp = temp.children[folder]

        return temp.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
