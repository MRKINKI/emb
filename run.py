from main.data import EMBDataSet
from config import Config
from main.models import get_class


def run_build_corpus(opts):
    eds = EMBDataSet(opts)
    eds.write2txt()


def run_embedding(opts):
    emb_model = get_class(opts.emb_method)(opts)
    emb_model.train()


if __name__ == '__main__':
    # run_build_corpus(Config)
    run_embedding(Config)
