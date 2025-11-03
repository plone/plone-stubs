from _typeshed import Incomplete

BLANKS_REGEX: Incomplete

def unidiff(
    a,
    b,
    filename_a: bytes = b"original",
    timestamp_a: bytes = b"",
    filename_b: bytes = b"modified",
    timestamp_b: bytes = b"",
    ignore_blanks: bool = False,
):
    """Compare two sequences of lines; generate the resulting delta.

    Each sequence must contain individual single-line strings
    ending with newlines. Such sequences can be obtained from the
    `readlines()` method of file-like objects.  The delta
    generated also consists of newline-terminated strings, ready
    to be printed as-is via the writeline() method of a file-like
    object.

    Note that the last line of a file may *not* have a newline;
    this is reported in the same way that GNU diff reports this.
    *This method only supports UNIX line ending conventions.*

        filename_a and filename_b are used to generate the header,
        allowing other tools to determine what 'files' were used
        to generate this output.

        timestamp_a and timestamp_b, when supplied, are expected
        to be last-modified timestamps to be inserted in the
        header, as floating point values since the epoch.

    """

class ConfigDiff:
    security: Incomplete
    def __init__(
        self,
        lhs,
        rhs,
        missing_as_empty: bool = False,
        ignore_blanks: bool = False,
        skip=...,
    ) -> None: ...
    @security.private
    def compareDirectories(self, subdir=None): ...
    @security.private
    def compareFiles(self, filename, subdir=None): ...
    @security.private
    def compare(self): ...
