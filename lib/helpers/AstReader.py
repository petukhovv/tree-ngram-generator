import json


class AstReader:
    @staticmethod
    def read(filename):
        f = open(filename, 'r')
        nodes = f.read()
        f.close()
        loaded = json.loads(nodes)
        return loaded[0] if len(loaded) > 0 else []
