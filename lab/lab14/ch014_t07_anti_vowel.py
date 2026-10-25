def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for cahr in text:
        if char not in vowels:
            result = result+char
    return result
