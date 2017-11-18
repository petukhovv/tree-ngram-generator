from copy import copy


class NgramGenerator:
    def __init__(self, ast, n, max_distance=None):
        self.ast = ast
        self.n = n
        self.distance = max_distance

    def ngrams_recurrent_build(self, n, ngrams_on_path, node_type):
        """
        Recurrent n-grams building: append of current node type to n-grams of previous nodes
            (according to max distance).

        :param n: n in n-gram (n-gram order)
        :param ngrams_on_path: temporary n-gram list for nodes, which are on the current path
        :param node_type: current node type

        :return: appendant 'n-grams on path' list
        """
        grams_on_path = []
        i = 0

        for ngrams in reversed(ngrams_on_path):
            if self.distance is not None and i >= self.distance:
                continue
            if len(ngrams) < n:
                continue
            for gram in ngrams[n - 1]:
                gram_appendant = copy(gram)
                gram_appendant.append(node_type)
                grams_on_path.append(gram_appendant)
            i += 1

        return grams_on_path

    def walk(self, node, ngrams, depth=1):
        """
        AST walk.

        :param node: current node
        :param ngrams: object with n-gram arrays (temporary 'on_path' and finally 'all')
        :param depth: recursive depth

        :return:
        """
        n_bound = min(self.n, depth)
        ngrams_on_path_for_current = [None] * n_bound
        i = 1
        while i < n_bound:
            ngrams_on_path_for_current[i] = self.ngrams_recurrent_build(i, ngrams['on_path'], node['type'])
            i += 1

        ngrams_on_path_for_current[0] = [[node['type']]]
        ngrams['on_path'].append(ngrams_on_path_for_current)
        ngrams['all'].append(ngrams_on_path_for_current)

        if 'children' in node:
            for child_node in node['children']:
                ngrams = self.walk(child_node, ngrams, depth + 1)
                ngrams['on_path'].pop()

        return ngrams

    def generate(self):
        """
        Run n-gram generator.

        :return: found n-grams
        """
        ngrams = self.walk(self.ast[0], {'all': [], 'on_path': []})

        return ngrams['all']
