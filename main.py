import json

from pprint import pprint

from lib.NgramGenerator import NgramGenerator

f = open('2.json', 'r')
ast_json = f.read()
f.close()
ast = json.loads(ast_json)

ngram_generator = NgramGenerator(ast, n=3, max_distance=2)
ngrams = ngram_generator.generate()

pprint(ngrams)
