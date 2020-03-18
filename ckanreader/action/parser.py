import contextlib

import pandas as pd
import chardet

from ckanreader.settings import AppConfig


class ResourceParser:

    @classmethod
    def exec(cls, file_path: str, format: str):
        # ファイルタイプで判定
        if format.upper() == "CSV":
            chunk_size = AppConfig.ENCODE_CHECK_SIZE
            with open(file_path, 'rb') as f, contextlib.closing(chardet.UniversalDetector()) as detector:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    # chunk_sizeずつfeed
                    detector.feed(chunk)
                    # 推定結果が定まるとdetector.doneがTrueになる
                    if detector.done:
                        break
            encoding = detector.result['encoding']
            df = pd.read_csv(file_path, index_col=0, encoding=encoding.lower())
            return df.to_dict()

        elif format.upper() == "XLS" or format.upper() == "XLSX":
            df = pd.read_excel(file_path, index_col=0)
            return df.to_dict()
        else:
            return None
