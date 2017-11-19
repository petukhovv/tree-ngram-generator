import os
import json


class NgramWriter:
    @staticmethod
    def write(path, filename, ngrams_config):
        basename = os.path.basename(filename)
        dirname = path + '/' + os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        f = open(dirname + '/' + basename, 'w')
        f.write(json.dumps(ngrams_config))
        f.close()
