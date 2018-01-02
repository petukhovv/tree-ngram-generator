import argparse
import json

from lib.NGramsExtractor import NGramsExtractor

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.AstReader import AstReader
from lib.helpers.TimeLogger import TimeLogger

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with ASTs')
parser.add_argument('--output_file', '-o', nargs=1, type=str, help='Output file, which will contain extracted features')
args = parser.parse_args()

input_folder = args.input_folder[0]
output_file = args.output_file[0]

params = {
   'n': 3,
   'max_distance': 3,
   'no_normalize': True,
   'exclude': [['FUN']]
}

output = {
    'ngrams': {},
    'counter': 0
}


def ast_file_process(filename, output):
    time_logger = TimeLogger()

    root = AstReader.read(filename)
    extractor = NGramsExtractor()
    feature_values = extractor.extract(root, params)
    output['ngrams'] = {**output['ngrams'], **feature_values}
    output['counter'] += 1

    processed_time = time_logger.finish()
    print(str(output['counter']) + ' file is processed, time: ' + str(processed_time) + ', ' +
          str(len(list(feature_values))) + ' features extracted')


time_logger = TimeLogger()

FilesWalker.walk(input_folder, lambda filename: ast_file_process(filename, output))

with open(output_file, 'w') as f:
    f.write(json.dumps(output['ngrams'], default=str))

total_processed_time = time_logger.finish()
print('==================================')
print(str(output['counter']) + ' files processed, total time: ' + str(total_processed_time) + ', ' +
      str(len(list(output['ngrams']))) + ' features extracted')
