from _typeshed import Incomplete

import io

LANCZOS: Incomplete
logger: Incomplete
MAX_HEIGHT: int
FLOAT_RE: Incomplete

def none_as_int(the_int):
    """For python 3 compatibility, to make int vs. none comparison possible
    without changing the algorithms below.

    This should mimic python2 behaviour."""

MAX_PIXELS: Incomplete

def scaleImage(
    image,
    width=None,
    height=None,
    mode: str = "scale",
    quality: int = 88,
    result=None,
    direction=None,
):
    """Scale the given image data to another size and return the result
    as a string or optionally write in to the file-like `result` object.

    The `image` parameter can either be the raw image data (ie a `str`
    instance) or an open file.

    The `quality` parameter can be used to set the quality of the
    resulting image scales.

    The return value is a tuple with the new image, the image format and
    a size-tuple.  Optionally a file-like object can be given as the
    `result` parameter, in which the generated image scale will be stored.

    The `width`, `height`, `mode` parameters will be passed to
    :meth:`scalePILImage`, which performs the actual scaling.

    The generated image is a JPEG image, unless the original is a WEBP, PNG
    or GIF image. This is needed to make sure alpha channel information is
    not lost, which JPEG does not support.
    """

def scaleSingleFrame(image, width, height, mode, format_, quality, direction): ...
def get_scale_mode(mode, direction=None): ...

class ScaledDimensions:
    final_width: Incomplete
    final_height: Incomplete
    factor_width: float
    post_scale_crop: bool
    pre_scale_crop: bool
    def __init__(self, original_width: int = 0, original_height: int = 0) -> None: ...

def calculate_scaled_dimensions(
    original_width, original_height, width, height, mode: str = "scale"
):
    """Calculate the scaled image dimensions from the originals using the
    same logic as scalePILImage"""

def scalePILImage(image, width=None, height=None, mode: str = "scale", direction=None):
    """Scale a PIL image to another size.

    This is all about scaling for the display in a web browser.

    Either width or height - or both - must be given.

    Three different scaling options are supported via `mode` and correspond to
    the CSS background-size values
    (see https://developer.mozilla.org/en-US/docs/Web/CSS/background-size):

    `contain`
        Alternative spellings: `scale-crop-to-fit`, `down`.
        Starts by scaling the relatively smallest dimension to the required
        size and crops the other dimension if needed.

    `cover`
        Alternative spellings: `scale-crop-to-fill`, `up`.
        Scales the relatively largest dimension up to the required size.
        Despite the alternative spelling, I see no cropping happening.

    `scale`
        Alternative spellings: `keep`, `thumbnail`.
        Scales to the requested dimensions without cropping. The resulting
        image may have a different size than requested. This option
        requires both width and height to be specified.
        Does not scale up.

    The `image` parameter must be an instance of the `PIL.Image` class.

    The return value the scaled image in the form of another instance of
    `PIL.Image`.
    """

def scale_svg_image(
    image: io.BytesIO,
    target_width: None | int,
    target_height: None | int,
    mode: str = "contain",
) -> tuple[bytes, tuple[int, int]]:
    """Scale and crop a SVG image to another display size.

    This is all about scaling for the display in a web browser.

    Either width or height - or both - must be given.

    Three different scaling options are supported via `mode` and correspond to
    the CSS background-size values
    (see https://developer.mozilla.org/en-US/docs/Web/CSS/background-size):

    `contain`
        Alternative spellings: `scale-crop-to-fit`, `down`.
        Starts by scaling the relatively smallest dimension to the required
        size and crops the other dimension if needed.

    `cover`
        Alternative spellings: `scale-crop-to-fill`, `up`.
        Scales the relatively largest dimension up to the required size.
        Despite the alternative spelling, I see no cropping happening.

    `scale`
        Alternative spellings: `keep`, `thumbnail`.
        Scales to the requested dimensions without cropping. The resulting
        image may have a different size than requested. This option
        requires both width and height to be specified.
        Does scale up.

    The `image` parameter must be bytes of the SVG, utf-8 encoded.

    The return value the scaled bytes in the form of another instance of
    `PIL.Image`.
    """
