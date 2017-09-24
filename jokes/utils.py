from nltk.tokenize import RegexpTokenizer

def get_word_count(text):
    """get the word count of a joke"""
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return len(tokens)
