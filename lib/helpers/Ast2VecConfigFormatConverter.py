class Ast2VecConfigFormatConverter:
    @staticmethod
    def convert(ngrams, max_distance):
        features = []

        for grams_by_n in ngrams:
            n = 1
            for grams in grams_by_n:
                for gram in grams:
                    features.append({
                        'type': 'ngram',
                        'params': {
                            'name': ':'.join(gram),
                            'node_types': gram,
                            'max_distance': max_distance
                        }
                    })
                n += 1

        return features
