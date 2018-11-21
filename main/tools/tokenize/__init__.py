from .corenlp_tokenizer import CoreNLPTokenizer
from .charater_segment import CharaterSegment


def get_class(name):
    if name == 'corenlp':
        return CoreNLPTokenizer
    elif name == 'character':
        return CharaterSegment
