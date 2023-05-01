from datetime import datetime
from abc import ABC, abstractmethod

class Node(ABC):
    """ 
    Base Node class. To be extended as a CodeNode or a FolderNode based on the file type.
    """
    description = ''

    def __init__(self, name, path, parent) -> None:
        self.updated_time = datetime.now()
        self.name = name
        self.parent = parent
        self.path = path
        self.children = {}
        print(self.path)
    
    @abstractmethod
    def generate_description(self):
        pass