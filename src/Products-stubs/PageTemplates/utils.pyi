from _typeshed import Incomplete

xml_preamble_reg: Incomplete
http_equiv_reg: Incomplete
http_equiv_reg2: Incomplete

def encodingFromXMLPreamble(xml, default=...):
    """Extract the encoding from a xml preamble.
    Expects XML content is binary (encoded), otherwise a previous
    transport encoding is meaningless.
    Return 'utf-8' if not available
    """

def charsetFromMetaEquiv(html):
    """Return the value of the \'charset\' from a html document containing
    <meta http-equiv="content-type" content="text/html; charset=utf8>.
    Expects HTML content is binary (encoded), otherwise a previous
    transport encoding is meaningless.
    Returns None, if not available.
    """

def convertToUnicode(source, content_type, preferred_encodings):
    """Convert a binary 'source' to the unicode (text) type.
    Attempts to detect transport encoding from XML and html
    documents, falling back to preferred_encodings.
    Returns (unicode_str, source_encoding).
    """
