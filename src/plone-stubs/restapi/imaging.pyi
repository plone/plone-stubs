from _typeshed import Incomplete

scale_parameter: Incomplete

def get_scales(context, field, width, height):
    """Get a dictionary of available scales for a particular image field,
    with the actual dimensions (aspect ratio of the original image).
    """

def get_original_image_url(context, fieldname, width, height): ...
def get_actual_scale(dimensions, bbox):
    """Given dimensions of an original image, and a bounding box of a scale,
    calculates what actual dimensions that scaled image would have,
    maintaining aspect ratio.

    This is supposed to emulate / predict the behavior of Plone's
    ImageScaling implementations.
    """

def get_scale_infos():
    """Returns a list of (name, width, height) 3-tuples of the
    available image scales.
    """
