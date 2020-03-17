
import os


class AppConfig:

    DOWNLOAD_PATH = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "downloads")

    ENCODE_CHECK_SIZE = 100
