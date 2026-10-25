def censor(text, word):
    new_words = text.split()
    result_list = []
    for item in new_words:
        if item == word:
            stars = '*' len(word)
            result_list.append(stars)
        else:
            result_list.append(new_words)
    
    return ' '.join(result_list)
    
