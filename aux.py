def find_word(word : str, vocab):
    item = [i for i in range(len(vocab)) if vocab[i]['ita'] == word.lower()]
    return item[0]


