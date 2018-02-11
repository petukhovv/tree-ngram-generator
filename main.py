import argparse
import json

from lib.NGramsExtractor import NGramsExtractor

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.AstReader import AstReader
from lib.helpers.TimeLogger import TimeLogger

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with ASTs')
parser.add_argument('--output_file', '-o', nargs=1, type=str, help='output file, which will contain extracted features')
args = parser.parse_args()

input_folder = args.input_folder[0]
output_file = args.output_file[0]

params = {
   'n': 3,
   'max_distance': 3,
   'no_normalize': True
}

output = {
    'ngrams': {}
}


def ast_file_process(filename, output):
    time_logger = TimeLogger(task_name='Processing %s file' % filename)

    root = AstReader.read(filename)
    extractor = NGramsExtractor()
    feature_values = extractor.extract(root, params)
    output['ngrams'] = {**output['ngrams'], **feature_values}

    time_logger.finish()


time_logger = TimeLogger(task_name='N-gram generating')

FilesWalker.walk(input_folder, lambda filename: ast_file_process(filename, output))

with open(output_file, 'w') as f:
    f.write(json.dumps(output['ngrams'], default=str))

time_logger.finish(full_finish=True)
print('%d n-grams generated' % len(list(output['ngrams'])))
print('-------------------')
