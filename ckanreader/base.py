from abc import ABCMeta, abstractmethod


class CkanRequest(metaclass=ABCMeta):
    @abstractmethod
    def gets(self):
        pass


class ResourceParser(metaclass=ABCMeta):
    @abstractmethod
    def parse(self):
        pass
