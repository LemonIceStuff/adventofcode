class Directory:
    def __init__(self, parent, child, files):
        self.parent = parent
        self.child = child
        self.files = files


class File:
    def __init__(self, size, parent):
        self.parent = parent
        self.size = size

