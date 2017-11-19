import sys
import os

from lib.NgramGenerator import NgramGenerator
from lib.helpers.Ast2VecConfigFormatConverter import Ast2VecConfigFormatConverter
from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.AstReader import AstReader
from lib.helpers.NgramWriter import NgramWriter

if len(sys.argv) <= 1:
    sys.stderr.write('ASTs folder not specified.\n')
    exit()

if len(sys.argv) <= 2:
    sys.stderr.write('Max gram order not specified (n in n-gram).\n')
    exit()

if len(sys.argv) <= 3:
    sys.stderr.write('Max n-gram distance not specified.\n')
    exit()

if len(sys.argv) <= 4:
    sys.stderr.write('Folder output (with n-gram configs) not specified.\n')
    exit()

folder_input = sys.argv[1]
n = int(sys.argv[2])
max_distance = int(sys.argv[3])
folder_output = sys.argv[4]


def ast_file_process(filename):
    root = AstReader.read(filename)

    ngram_generator = NgramGenerator(root, n, max_distance)
    ngrams = ngram_generator.generate()

    feartures = Ast2VecConfigFormatConverter.convert(ngrams, max_distance)

    relative_filename = os.path.relpath(filename, folder_input)
    NgramWriter.write(folder_output, relative_filename, feartures)


FilesWalker.walk(folder_input, ast_file_process)
