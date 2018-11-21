from gensim.models import Word2Vec
from .utils import Sentences


class BuildWord2Vec:
    def __init__(self, opts):
        self.opts = opts
        self.sentences = Sentences(opts)

    def train(self):

        model = Word2Vec(self.sentences,
                         size=100,
                         window=5,
                         min_count=3,
                         sample=1e-3,
                         workers=5,
                         negative=5,
                         hs=0,
                         iter=15)
        model.save(self.opts.emb_path)
