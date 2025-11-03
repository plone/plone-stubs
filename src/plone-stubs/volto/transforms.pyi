from _typeshed import Incomplete
from collections.abc import Generator
from plone.restapi.deserializer.blocks import ResolveUIDDeserializerBase
from plone.restapi.serializer.blocks import ResolveUIDSerializerBase

class NestedBlocksVisitor:
    """Visit nested blocks in columns, hrefList, or slides."""
    def __init__(self, context, request) -> None: ...
    def __call__(self, block_value) -> Generator[Incomplete, Incomplete]: ...

class NestedResolveUIDDeserializerBase:
    """The "url" smart block field for nested blocks

    [Deprecated -- replaced by NestedBlocksVisitor above,
    but the base class is still here in case someone extended it.]

    This is a generic handler. In all blocks, it converts any "url"
    field from using resolveuid to an "absolute" URL
    """

    order: int
    block_type: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class NestedResolveUIDSerializerBase:
    """
    [Deprecated -- replaced by NestedBlocksVisitor above,
    but the base class is still here in case someone extended it.]
    """

    order: int
    block_type: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class PreviewImageResolveUIDDeserializer(ResolveUIDDeserializerBase):
    """Deserializer for resolveuid in preview_image field"""

    fields: Incomplete

class PreviewImageResolveUIDDeserializerRoot(ResolveUIDDeserializerBase):
    """Deserializer for resolveuid in preview_image field on site root"""

    fields: Incomplete

class PreviewImageResolveUIDSerializer(ResolveUIDSerializerBase):
    """Serializer for resolveuid in preview_image field"""

    fields: Incomplete

class PreviewImageResolveUIDSerializerRoot(ResolveUIDSerializerBase):
    """Serializer for resolveuid in preview_image field on site root"""

    fields: Incomplete
