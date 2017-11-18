import json

from pprint import pprint

from lib.NgramGenerator import NgramGenerator
from lib.helpers.Ast2VecConfigFormatConverter import Ast2VecConfigFormatConverter

f = open('1.json', 'r')
ast_json = f.read()
f.close()
ast = json.loads(ast_json)

max_distance = 2

ngram_generator = NgramGenerator(ast, n=3, max_distance=max_distance)
ngrams = ngram_generator.generate()

feartures = Ast2VecConfigFormatConverter.convert(ngrams, max_distance)

f = open('result.json', 'w')
f.write(json.dumps(feartures))
f.close()
