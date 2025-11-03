from _typeshed import Incomplete
from plone.restapi.deserializer.blocks import SlateBlockTransformer
from plone.restapi.serializer.dxfields import DefaultFieldSerializer

class BlocksJSONFieldSerializer(DefaultFieldSerializer):
    def __call__(self): ...

class ResolveUIDSerializerBase:
    order: int
    block_type: Incomplete
    fields: Incomplete
    disabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class TextBlockSerializerBase:
    order: int
    block_type: str
    disabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, value): ...

class ResolveUIDSerializer(ResolveUIDSerializerBase):
    """UID-to-URL transformer for all content types"""

class ResolveUIDSerializerRoot(ResolveUIDSerializerBase):
    """Serializer for site root"""

class TextBlockSerializer(TextBlockSerializerBase):
    """Serializer for content-types with IBlocks behavior"""

class TextBlockSerializerRoot(TextBlockSerializerBase):
    """Serializer for site root"""

class SlateBlockSerializerBase(SlateBlockTransformer):
    """SlateBlockSerializerBase."""

    order: int
    block_type: str
    disabled: Incomplete
    def handle_a(self, child) -> None: ...
    def handle_link(self, child) -> None: ...

class SlateBlockSerializer(SlateBlockSerializerBase):
    """Serializer for content-types with IBlocks behavior"""

class SlateBlockSerializerRoot(SlateBlockSerializerBase):
    """Serializer for site root"""

class SlateTableBlockSerializerBase(SlateBlockSerializerBase):
    """SlateBlockSerializerBase."""

    order: int
    block_type: str
    def __call__(self, block):
        """call"""

class SlateTableBlockSerializer(SlateTableBlockSerializerBase):
    """Serializer for content-types with IBlocks behavior"""

class SlateTableBlockSerializerRoot(SlateTableBlockSerializerBase):
    """Serializer for site root"""

class TeaserBlockSerializerBase:
    order: int
    block_type: str
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

class TeaserBlockSerializer(TeaserBlockSerializerBase):
    """Serializer for content-types with IBlocks behavior"""

RESOLVE_UID_REGEXP: Incomplete

class TeaserBlockSerializerRoot(TeaserBlockSerializerBase):
    """Serializer for site root"""

def url_to_brain(url):
    """Find the catalog brain for a URL.

    Returns None if no item was found that is visible to the current user.
    """
