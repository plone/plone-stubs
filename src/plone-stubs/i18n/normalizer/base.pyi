from _typeshed import Incomplete

whitespace: Incomplete
allowed: Incomplete

def mapUnicode(text, mapping=()):
    """
    This method is used for replacement of special characters found in a
    mapping before baseNormalize is applied.
    """

def baseNormalize(text):
    """
    This method is used for normalization of unicode characters to the base
    ASCII letters.
    Output is a native string with only ASCII letters, digits, punctuation
    and whitespace characters. Case is preserved.

      >>> baseNormalize(123)
      \'123\'

      >>> baseNormalize(u\'a\u0fff\')
      \'a\'

      >>> baseNormalize(u"fooǏ")
      \'fooI\'

      >>> baseNormalize(u"北亰")
      \'Bei Jing\'
    """
