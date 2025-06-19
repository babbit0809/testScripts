import os
import json


class JsonReader(object):
    def __init__(self, path):
        self._data = None
        if os.path.exists(path):
            self.file = path

        else:
            raise FileNotFoundError("Target file not exist in this path.")

    @property
    def read_file(self):
        if not self._data:
            with open(self.file, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
        return self._data


if __name__ == '__main__':
    pass
