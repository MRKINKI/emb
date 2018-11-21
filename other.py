from main.tools.tokenize import get_class
from gensim.models import Word2Vec
from config import Config


if __name__ == '__main__':
    question = '水果有哪些品种'
    tokenizer = get_class('character')()
    tokens = tokenizer.segment(question)
    # print(tokens)

    model = Word2Vec.load(Config.emb_path)
    print(model.most_similar('鱼'))

    with open(Config.vocab_path, 'w', encoding='utf-8') as fin:
        fin.write('<S>' + '\n')
        fin.write('</S>' + '\n')
        fin.write('<UNK>' + '\n')
        for word in model.wv.vocab:
            fin.write(word + '\n')
