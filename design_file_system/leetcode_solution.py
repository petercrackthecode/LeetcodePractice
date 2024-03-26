# https://leetcode.com/problems/design-file-system
class FileSystem:
    def __init__(self):
        self.file_system = {}

    def createPath(self, path, value):
        ans = path.replace("/", " /").split()
        parent_dir = "".join(ans[:-1])

        if parent_dir:
            if parent_dir in self.file_system and path not in self.file_system:
                self.file_system[path] = value
                return True
        else:
            # parent_dir is empty
            if path not in self.file_system:
                self.file_system[path] = value
                return True

        return False

    def get(self, path):
        return self.file_system.get(path, -1)
