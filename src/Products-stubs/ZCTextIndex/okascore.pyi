B: float
B_FROM1: float
K1: float
K1_PLUS1: float

def score(result, d2fitems, d2len, idf, meandoclen) -> None:
    """
    Do the inner scoring loop for an Okapi index.

    result: IIBucket result, maps d to score
    d2fitems: _wordinfo[t].items(), maps d to f(d, t)
    d2len: _docweight, maps d to # words in d
    idf: inverse doc frequency of t
    meandoclen: average number of words in a doc

    BBB ZCTextIndex 4.0: Compatibility for former C implementation.
    """
