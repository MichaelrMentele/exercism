def is_pangram(sentence):
    """
    Check if string is a pangram. A pangram contains every letter of the alphabet
    at least once.
    :params sentence:str
    :return bool
    """
    if len(sentence) < 26: return False

    sentence = sentence.lower()

    has_been_seen = {}
    for c in sentence:
        if c.isalpha():
            has_been_seen[c] = True
        if len(has_been_seen) == 26:
            return True

    return False
