def censor(text, word):
    new_words = text.split()
    result_list = []
    for item in new_words:
        if item == word:
            stars = '*' len(word)
            return '*' len(word)
        else:
            return item
        return append.new_words
