import pandas as pd

from ckanreader.base import ResourceParser


class CsvParser(ResourceParser):

    def __init__(self, file_path: str, encoding: str, format: str):
        self.file_path = file_path
        self.encoding = encoding
        self.format = format

    def parse(self):
        df = pd.read_csv(
            self.file_path, index_col=0, encoding=self.encoding)
        return df.to_dict()


class ExcelParser(ResourceParser):

    def __init__(self, file_path: str, format: str):
        self.file_path = file_path
        self.encoding = encoding
        self.format = format

    def parse(self):
        df = pd.read_excel(
            self.file_path, index_col=0, encoding=self.encoding)
        return df.to_dict()


class PdfParser:

    def __init__(self, file_path: str, format: str):
        self.file_path = file_path
        self.format = format
