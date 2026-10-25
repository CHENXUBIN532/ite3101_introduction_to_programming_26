def censor(text,word):
    new_words = text.split()
    for item in new_words:
        if item == word:
            return 