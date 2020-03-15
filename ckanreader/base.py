from abc import ABCMeta, abstractmethod


class CkanRequest(metaclass=ABCMeta):
    @abstractmethod
    def gets(self):
        pass
