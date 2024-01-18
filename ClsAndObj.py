class BaseClass :
    def __init__(self, Id, Name):
        self.ID = Id
        self.NAME = Name

class DirClass (BaseClass):
    def __init__(self, Id, Name, Dir):
        super().__init__(Id, Name)
        self.DIR = Dir
        print(self.ID)
        print(self.NAME)
        print(self.DIR)
        