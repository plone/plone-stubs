class UTF8EncodingConflictResolver:
    """This resolver tries to decode a string from utf-8 and replaces it
    otherwise but logs a warning.
    """
    def resolve(self, context, text, expression): ...
