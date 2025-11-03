def unique(iterable): ...
def cleanId(id):
    """'url_quote' turns strange chars into '%xx', which is not a valid char
    for ObjectManager. Here we encode '%' into '-' (and '-' into '--' as
    escaping).
    De-clean is possible; see 'decleanId'.
    Assumes that id can start with non-alpha(numeric), which is true.
    """

def decleanId(id):
    """Reverse cleanId."""

def scale_image(image_file, max_size=None, default_format=None):
    """Scales an image down to at most max_size preserving aspect ratio
    from an input file

        >>> from Products.PlonePAS import config
        >>> from pathlib import Path
        >>> from io import BytesIO
        >>> from Products.PlonePAS.utils import scale_image
        >>> from PIL import Image

    Let\'s make a couple test images and see how it works (all are
    100x100), the gif is paletted mode::

        >>> pas_path = Path(config.__file__).parent
        >>> path = pas_path / \'tests\' / \'images\'
        >>> orig_jpg = (path / \'test.jpg\').open(\'rb\')
        >>> orig_png = (path / \'test.png\').open(\'rb\')
        >>> orig_gif = (path / \'test.gif\').open(\'rb\')

    We\'ll also make some evil non-images, including one which
    masquerades as a jpeg (which would trick OFS.Image)::

        >>> invalid = BytesIO(\'<div>Evil!!!</div>\'.encode("utf-8"))
        >>> sneaky = BytesIO(\'ÿØ<div>Evil!!!</div>\'.encode("utf-8"))

    OK, let\'s get to it, first check that our bad images fail:

        >>> try:
        ...     scale_image(invalid, (50, 50))
        ... except Exception as e:
        ...     print(e)
        cannot identify image file...

        >>> try:
        ...     scale_image(sneaky, (50, 50))
        ... except Exception as e:
        ...     print(e)
        cannot identify image file...

    Now that that\'s out of the way we check on our real images to make
    sure the format and mode are preserved, that they are scaled, and that they
    return the correct mimetype::

        >>> new_jpg, mimetype = scale_image(orig_jpg, (50, 50))
        >>> img = Image.open(new_jpg)
        >>> img.size
        (50, 50)
        >>> img.format
        \'JPEG\'
        >>> mimetype
        \'image/jpeg\'

        >>> new_png, mimetype = scale_image(orig_png, (50, 50))
        >>> img = Image.open(new_png)
        >>> img.size
        (50, 50)
        >>> img.format
        \'PNG\'
        >>> mimetype
        \'image/png\'

        >>> new_gif, mimetype = scale_image(orig_gif, (50, 50))
        >>> img = Image.open(new_gif)
        >>> img.size
        (50, 50)
        >>> img.format
        \'GIF\'
        >>> img.mode
        \'P\'
        >>> mimetype
        \'image/gif\'

    We should also preserve the aspect ratio by scaling to the given
    width only unless told not to (we need to reset out files before
    trying again though::

        >>> _ = orig_jpg.seek(0)
        >>> new_jpg, mimetype = scale_image(orig_jpg, (70, 100))
        >>> img = Image.open(new_jpg)
        >>> img.size
        (70, 70)

        >>> _ = orig_jpg.seek(0)
        >>> new_jpg, mimetype = scale_image(orig_jpg, (70, 50))
        >>> img = Image.open(new_jpg)
        >>> img.size
        (50, 50)

        >>> orig_jpg.close()
        >>> orig_png.close()
        >>> orig_gif.close()

    """

def getGroupsForPrincipal(principal, plugins, request=None): ...

class CleanupTemp:
    """Used to cleanup _v_temps at the end of the request."""
    def __init__(self, tool) -> None: ...
    def __del__(self) -> None: ...
