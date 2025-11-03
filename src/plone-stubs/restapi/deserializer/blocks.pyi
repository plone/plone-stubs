from _typeshed import Incomplete
from collections.abc import Generator
from plone.restapi.deserializer.dxfields import DefaultFieldDeserializer

def iterate_children(value) -> Generator[Incomplete]:
    """iterate_children.

    :param value:
    """

class BlocksJSONFieldDeserializer(DefaultFieldDeserializer):
    def __call__(self, value): ...

class ResolveUIDDeserializerBase:
    """The "url" smart block field.

    This is a generic handler. In all blocks, it converts any "url"
    field from using resolveuid to an "absolute" URL
    """

    order: int
    block_type: Incomplete
    fields: Incomplete
    disabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class TextBlockDeserializerBase:
    order: int
    block_type: str
    disabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class HTMLBlockDeserializerBase:
    order: int
    block_type: str
    disabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class ImageBlockDeserializerBase:
    order: int
    block_type: str
    disabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class ResolveUIDDeserializer(ResolveUIDDeserializerBase):
    """URL-to-UID transformer for all content types"""

class ResolveUIDDeserializerRoot(ResolveUIDDeserializerBase):
    """Deserializer for site root"""

class TextBlockDeserializer(TextBlockDeserializerBase):
    """Deserializer for content-types that implements IBlocks behavior"""

class TextBlockDeserializerRoot(TextBlockDeserializerBase):
    """Deserializer for site root"""

class HTMLBlockDeserializer(HTMLBlockDeserializerBase):
    """Deserializer for content-types that implements IBlocks behavior"""

class HTMLBlockDeserializerRoot(HTMLBlockDeserializerBase):
    """Deserializer for site root"""

class ImageBlockDeserializer(ImageBlockDeserializerBase):
    """Deserializer for content-types that implements IBlocks behavior"""

class ImageBlockDeserializerRoot(ImageBlockDeserializerBase):
    """Deserializer for site root"""

def transform_links(context, value, transformer) -> None:
    """Convert absolute links to resolveuid
    http://localhost:55001/plone/link-target
    ->
    ../resolveuid/023c61b44e194652804d05a15dc126f4"""

class SlateBlockTransformer:
    """SlateBlockTransformer."""

    field: str
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class SlateBlockDeserializerBase(SlateBlockTransformer):
    """SlateBlockDeserializerBase."""

    order: int
    block_type: str
    disabled: Incomplete
    def handle_a(self, child) -> None: ...
    def handle_link(self, child) -> None: ...

class SlateBlockDeserializer(SlateBlockDeserializerBase):
    """Deserializer for content-types that implements IBlocks behavior"""

class SlateBlockDeserializerRoot(SlateBlockDeserializerBase):
    """Deserializer for site root"""

class SlateTableBlockTransformer(SlateBlockTransformer):
    def __call__(self, block): ...

class SlateTableBlockDeserializerBase(
    SlateTableBlockTransformer, SlateBlockDeserializerBase
):
    """SlateTableBlockDeserializerBase."""

    order: int
    block_type: str

class SlateTableBlockDeserializer(SlateTableBlockDeserializerBase):
    """Deserializer for content-types that implements IBlocks behavior"""

class SlateTableBlockDeserializerRoot(SlateTableBlockDeserializerBase):
    """Deserializer for site root"""
