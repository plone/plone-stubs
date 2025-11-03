def closest_content(context=None):
    """Try to find a usable context, with increasing aggression"""

def call_callables(value, *args, **kwargs):
    """Walk recursively through data structure and call all callables, passing
    the arguments and keyword arguments to it.
    """

def replace_link_variables_by_paths(context, url):
    """Take an `url` and replace the variables "${navigation_root_url}" and
    "${portal_url}" by the corresponding paths. `context` is the acquisition
    context.
    """

def is_absolute(url):
    """Return ``True``, if url is an absolute url.
    See: https://stackoverflow.com/a/8357518/1337474
    """

def is_same_domain(url1, url2):
    """Return ``True``, if url1 is on the same protocol and domain than url2."""

def dict_merge(dict_a, dict_b):
    """Helper method which merges two dictionaries.

    Recursively merges dict's. not just simple a['key'] = b['key'], if
    both a and b have a key who's value is a dict then dict_merge is called
    on both values and the result stored in the returned dictionary.

    http://www.xormedia.com/recursively-merge-dictionaries-in-python

    :param dict_a: [required] First dictiornary.
    :type dict_a: dict

    :param dict_b: [required] Second dictiornary.
    :type dict_b: dict

    :returns: Merged dictionary.
    :rtype: dict
    """

def get_widget_form(widget): ...
def get_portal(): ...
def get_portal_url(context): ...
def get_context_url(context): ...
def remove_invalid_xml_characters(txt): ...
