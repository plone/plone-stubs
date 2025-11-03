from _typeshed import Incomplete
from collections.abc import Iterable
from OFS.Image import extract_media_type as extract_media_type

QUALITY_DEFAULT: int
pattern: Incomplete
log: Incomplete

class filestream_range_iterator(Iterable):
    """
    A class that mimics FileIO and implements an iterator that returns a
    fixed-sized sequence of bytes. Beginning from `start` to `end`.

    BBB: due to a possible bug in Zope>4, <=4.1.3, couldn't be subclass of FileIO
         as Iterators.filestream_iterator
    """

    streamsize: Incomplete
    start: Incomplete
    end: Incomplete
    def __init__(
        self,
        name,
        mode: str = "rb",
        bufsize: int = -1,
        streamsize=...,
        start: int = 0,
        end=None,
    ) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__
    def close(self) -> None: ...
    def read(self, size: int = -1): ...

def safe_basename(filename):
    """Get the basename of the given filename, regardless of which platform
    (Windows or Unix) it originated from.
    """

def get_contenttype(
    file=None, filename=None, default: str = "application/octet-stream"
):
    """Get the MIME content type of the given file and/or filename.

    Note: depending on your use case, you may want to call 'extract_media_type'
    on the result.
    """

def set_headers(file, response, filename=None, canonical=None) -> None:
    """Set response headers for the given file. If filename is given, set
    the Content-Disposition to attachment.
    """

def stream_data(file, start: int = 0, end=None):
    """Return the given file as a stream if possible."""

def getImageInfo(data): ...
def get_exif(image, content_type=None, width=None, height=None): ...
def rotate_image(image_data, method=None, REQUEST=None):
    """Rotate Image if it has Exif Orientation Information other than 1.

    Do not use PIL.Image.rotate function as this did not transpose the image,
    rotate keeps the image width and height and rotates the image around a
    central point. PIL.Image.transpose also changes Image Orientation.
    """

def getRetinaScales(): ...
def getHighPixelDensityScales(): ...
def getAllowedSizes(): ...
def getQuality(): ...
