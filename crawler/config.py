import os, sys, json
# from collections import namedtuple

# TODO:
# implementar conversão de json para python object


class Utils:
    def __init__(self, filename: str = None) -> None:
        self.filename = filename

    def get_json(self) -> str:

        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)

        sys.path.append(parent_dir)
        full_path = parent_dir + "/" + self.filename + ".json"

        print("Carregando arquivo de configuração: ", full_path, "\n")

        config = open(full_path)
        json_data = json.load(config)

        return json_data

class Secrets(Utils):
    def __init__(self) -> None:
        super().__init__("secrets")

    def read(self):
        return self.get_json()

class Config(Utils):
    def __init__(self) -> None:
        super().__init__("config")

    def read(self):
        return self.get_json()
