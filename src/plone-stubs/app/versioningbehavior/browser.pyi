from _typeshed import Incomplete

class VersionView:
    """Renders the content-core slot of a version of a content item.

    Currently it works by rendering the @@content-core view of the item and then converting the
    links that points to files and images to use the @@download-version view.

    Request parameters:

    version_id -- Version ID.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...

class DownloadVersion:
    """Downloads a file in a field of a content item at an specific version.


    Request parameters:

    version_id -- Version ID.
    field_id -- (optional) ID of the field (eg.: "file" or "image"). If omitted then the
                primary field will be used.
    filename -- (optional) Filename. If omitted then the filename HTTP header won\'t be set on the
                response, but the download will occur normally.
    do_not_stream -- (optional) Do not stream the file.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
