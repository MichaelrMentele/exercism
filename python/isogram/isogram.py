from collections import Counter

def is_isogram(word):
    """
    Determine if a word is an isogram. An isogram is a word where a character
    has a frequency of one or less.
    :params wors:str
    :return bool
    """
    alphabet_freq = Counter()
    for c in word.lower():
        if c.isalpha():
            alphabet_freq[c] += 1
            if alphabet_freq[c] > 1:
                return False

    return True

