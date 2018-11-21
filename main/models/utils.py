class Sentences:
    def __init__(self, opts):
        self.file_path = opts.file_path

    def __iter__(self):
        with open(self.file_path, encoding='utf-8') as fin:
            for line in fin:
                sentence_words = line.strip().split()
                yield sentence_words
