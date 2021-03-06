"""
Spelling Corrector in Python 3

"""

import re
from os import path
from collections import Counter


def words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open(path.join(path.dirname(path.abspath(__file__)), 'words.txt'), encoding='utf-8').read()))


def p(word, n=sum(WORDS.values())):
    """
    Probability of `word`.
    :param word:
    :param n:
    :return: float
    """
    return WORDS[word] / n


def correction(word):
    """
    Most probable spelling correction for word.
    :param word: str
    :return: max probability
    """
    return max(candidates(word), key=p)


def candidates(word):
    """
    Generate possible spelling corrections for word.
    :param word: str
    :return: set of known words
    """
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]


def known(words):
    """
    The subset of `words` that appear in the dictionary of WORDS.
    :param words: list of str
    :return: unique set of words
    """
    return set(w for w in words if w in WORDS)


def edits1(word):
    """
    All edits that are one edit away from `word`.
    :param word: String
    :return: set of words
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """
    All edits that are two edits away from `word`.
    :param word: string
    :return: string generator
    """
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
