from ckanreader.base import ResourceParser


class CsvParser(ResourceParser):

    def __init__(self, file_path: str, encoding: str, format: str):
        self.file_path = file_path
        self.encoding = encoding
        self.format = format

    def parse(self):
        print("csv parser")


class ExcelParser(ResourceParser):

    def __init__(self, file_path: str, format: str):
        self.file_path = file_path
        self.encoding = encoding
        self.format = format

    def parse(self):
        print("excel parser")


class PdfParser:

    def __init__(self, file_path: str, format: str):
        self.file_path = file_path
        self.format = format
