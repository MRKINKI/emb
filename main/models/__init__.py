from .w2v import BuildWord2Vec


def get_class(name):
    if name == 'word2vec':
        return BuildWord2Vec
