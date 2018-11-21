import pymongo


class Config:
    file_path = './data/character.txt'
    collection = pymongo.MongoClient('192.168.1.145', 27017).food['food_all_qa_pairs']
    tokenizer_type = 'character'
    emb_method = 'word2vec'
    emb_path = './data/word2vec.model'
    vocab_path = './data/vocab.txt'
