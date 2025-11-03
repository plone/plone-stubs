from _typeshed import Incomplete
from Products.Five.browser import BrowserView
from zope.browserresource.file import File

import zope.browserresource.directory
import zope.browserresource.file

class Resource:
    """A mixin that changes the URL-rendering of resources (__call__).

    In zope.browserresource, resource URLs are of the form
    nearest_site/@@/resource_name.  Since Zope 2 didn't have support
    for sites from the beginning of the Five integration, resource
    URLs in Zope 2 are of the form context/++resource++resource_name.

    TODO It would be good if that could be changed in the long term,
    thus making this mixin (and probably the other classes in this
    module) obsolete.
    """
    def __call__(self): ...

class PageTemplateResource(Resource, BrowserView):
    def browserDefault(self, request): ...
    def publishTraverse(self, request, name) -> None: ...
    def render(self):
        """Rendered content"""

class FileResource(Resource, zope.browserresource.file.FileResource): ...

class ResourceFactory:
    factory: Incomplete
    resource: Incomplete
    def __init__(self, name, path, resource_factory=None) -> None: ...
    def __call__(self, request): ...

class PageTemplateResourceFactory(ResourceFactory):
    """A factory for Page Template resources"""

    factory: Incomplete
    resource = PageTemplateResource

class FileResourceFactory(ResourceFactory):
    """A factory for File resources"""

    factory = File
    resource = FileResource

class ImageResourceFactory(ResourceFactory):
    """A factory for Image resources"""

    factory = File
    resource = FileResource

class Directory:
    path: Incomplete
    def __init__(self, path, name) -> None: ...

class DirectoryResource(Resource, zope.browserresource.directory.DirectoryResource):
    resource_factories: Incomplete
    default_factory = FileResourceFactory
    def getId(self): ...
    def get(self, name, default=...): ...

class DirectoryResourceFactory(ResourceFactory):
    factory = Directory
    resource = DirectoryResource
