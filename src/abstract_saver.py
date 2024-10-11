from abc import ABC, abstractmethod

class Saver(ABC):

    @abstractmethod
    def save_json(self):
        pass

    @abstractmethod
    def filter_data(self):
        pass