from _typeshed import Incomplete
from collections.abc import Generator

def bigram(u, limit: int = 1):
    """Split into bi-gram.
    limit arg describes ending process.
    If limit = 0 then
        日本人-> [日本,本人, 人]
        金 -> [金]
    If limit = 1 then
        日本人-> [日本,本人]
        金 -> []
    """

def process_str_post(s, enc: str = "utf-8"):
    """Receive str, remove ? and *, then return str.
    If decode gets successful, process str as str.
    If decode gets failed, process str as ASCII.
    """

def process_str(s, enc: str = "utf-8"):
    """Receive str and encoding, then return the list
    of str as bi-grammed result.
    Decode str into str and pass it to process_unicode.
    When decode failed, return the result split per word.
    Splitting depends on locale specified by rx_L.
    """

def process_str_glob(s, enc: str = "utf-8"):
    """Receive str and encoding, then return the list
    of str considering glob processing.
    Decode str into str and pass it to process_unicode_glob.
    When decode failed, return the result split per word.
    Splitting depends on locale specified by rxGlob_L.
    """

def process_unicode(uni) -> Generator[Incomplete, Incomplete]:
    """Receive unicode string, then return a list of unicode
    as bi-grammed result.
    """

def process_unicode_glob(uni) -> Generator[Incomplete, Incomplete]:
    """Receive unicode string, then return a list of unicode
    as bi-grammed result.  Considering globbing.
    """

class Splitter:
    def process(self, lst):
        """Will be called when indexing.
        Receive list of str, make it bi-grammed, then return
        the list of str.
        """
    def processGlob(self, lst):
        """Will be called once when searching.
        Receive list of str, make it bi-grammed considering
        globbing, then return the list of str.
        """
    def process_post_glob(self, lst):
        """Will be called twice when searching.
        Receive list of str, Remove ? and *, then return
        the list of str.
        """

class CaseNormalizer:
    def process(self, lst): ...

class I18NNormalizer:
    def process(self, lst): ...
