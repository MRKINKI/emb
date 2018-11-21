from .tools.tokenize import get_class
from gensim.models import Word2Vec


class EMBDataSet:
    def __init__(self, opts):
        self.qa_collection = opts.collection
        self.file_path = opts.file_path
        self.tokenizer = get_class(opts.tokenizer_type)()
        self.opts = opts

    def write2txt(self):
        url_set = set()
        with open(self.file_path, 'w', encoding='utf-8') as fout:
            for doc in self.qa_collection.find():
                question, answer, url = doc['question'], doc['answer'], doc['url']
                if url not in url_set:
                    url_set.add(url)
                    q_tokens = self.tokenizer.segment(question)
                    a_tokens = self.tokenizer.segment(answer)
                    fout.write(' '.join(q_tokens) + '\n')
                    fout.write(' '.join(a_tokens) + '\n')
        fout.close()

    def get_w2v_emb_text(self):
        model = Word2Vec.load(self.opts.emb_path)
        with open(self.opts.emb_text_path, 'w', encoding='utf-8') as fout:
            for vocab in model.wv.vocab:
                vocab_line_text_list = [vocab]
                vocab_vector = model.wv[vocab]
                vocab_line_text_list.extend(list(vocab_vector))
                vocab_line_text = ' '.join([str(t) for t in vocab_line_text_list])
                fout.write(vocab_line_text + '\n')
        fout.close()