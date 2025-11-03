from _typeshed import Incomplete

MANIFEST_FILENAME: str
LOGGER: Incomplete

class ManifestFormat:
    """Describes a manifest format.

    An immutable, threadsafe object.

    ``resourceType`` is used as the section header.

    ``keys`` should be a list of keys that should be returned.

    ``defaults`` can be used to pass a dict of default values. The keys
    should correspond to ``keys``, but it is not mandatory to fill every key.

    ``parameterSections`` can be a list section names in the ``manifest.cfg``
    file that can be used to supply additional, free-form parameters. For
    example, if ``parameters`` is ['parameters'] and 'resourceType' is
    'theme', then the ``manifest.cfg`` file may optionally contain a section
    ``[theme:parameters]``.
    """

    resourceType: Incomplete
    keys: Incomplete
    defaults: Incomplete
    parameterSections: Incomplete
    def __init__(
        self, resourceType, keys, defaults=None, parameterSections=None
    ) -> None: ...

def getManifest(fp, format, defaults=None):
    """Read the manifest from the given open file pointer according to the
    given ManifestFormat. Pass a dict as ``defaults`` to override the defaults
    from the manifest format.
    """

def extractManifestFromZipFile(zipfile, format, defaults=None, manifestFilename=...):
    """Get a resource name and manifest from the given open
    ``zipfile.ZipFile`` using the given format. Returns a tuple::

        (resourceName, manifestDict)

    Where ``resourceName`` is the resource name, taken to be the name of the
    single top level directory inside the zip file (ignoring certain OS
    files), and ``manifestDict`` is a dictionary as returned by
    ``getManifest()``.

    The ``manifestDict`` may be None if no manifest file was found.

    Will throw a ValueError if the zip file does not contain a single top
    level directory.

    Pass ``defaults`` to override the defaults from the manifest format.

    Pass ``manifestFilename`` to use a custom manifest filename.
    """

def getAllResources(format, defaults=None, filter=None, manifestFilename=...):
    """Get a dict of all resources of the resource type indicated by the
    manifest format. Returns a dict where the keys are the resource ids and
    the values are manifests. The value may be None if no manifest was found.

    Pass ``defaults`` to override the defaults from the manifest format.

    Pass ``filter``, a callable that takes a resource directory as its
    only argument, if you want to be able to filter out any resource
    directories. It should return True if the given directory should be
    included.

    Pass ``manifestFilename`` to use a different manifest file name
    convention.
    """

def getZODBResources(format, defaults=None, filter=None, manifestFilename=...):
    """Get a dict of all resources in the ZODB of the resource type indicated
    by the manifest format. Returns a dict where the keys are the resource
    ids and the values are manifests. The value may be None if no manifest was
    found.

    Pass ``defaults`` to override the defaults from the manifest format.

    Pass ``filter``, a callable that takes a resource directory as its
    only argument, if you want to be able to filter out any resource
    directories. It should return True if the given directory should be
    included.

    Pass ``manifestFilename`` to use a different manifest file name
    convention.
    """
