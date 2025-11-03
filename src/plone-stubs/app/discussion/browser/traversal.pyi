from _typeshed import Incomplete

class ConversationNamespace:
    """Allow traversal into a conversation via a ++conversation++name
    namespace. The name is the name of an adapter from context to
    IConversation. The special name 'default' will be taken as the default
    (unnamed) adapter. This is to work around a bug in OFS.Traversable which
    does not allow traversal to namespaces with an empty string name.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...
