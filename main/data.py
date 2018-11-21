from .tools.tokenize import get_class


class EMBDataSet:
    def __init__(self, opts):
        self.qa_collection = opts.collection
        self.file_path = opts.file_path
        self.tokenizer = get_class(opts.tokenizer_type)()

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
