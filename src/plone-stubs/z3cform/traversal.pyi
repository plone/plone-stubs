from _typeshed import Incomplete

class FormWidgetTraversal:
    """Allow traversal to widgets via the ++widget++ namespace. The context
    is the from itself (used when the layout wrapper view is not used).

    Note that to support security in Zope 2.10, the widget being traversed to
    must have an __of__ method, i.e. it must support acquisition. The easiest
    way to do that, is to mix in Acquisition.Explicit. The acquisition parent
    will be the layout form wrapper view.

    In Zope 2.12, this is not necessary, because we also set the __parent__
    pointer of the returned widget to be the traversal context.

    Unfortunately, if you mix in Acquisition.Explicit in Zope 2.12 *and* the
    class implements IAcquirer, Zope may complain because the view probably
    does *not* implement acquisition (in Zope 2.12, views no longer mix in
    Acquisition.Explicit). To support both Zope 2.10 and Zope 2.12, you will
    need to cheat and mix in Acquisition.Explicit, but use implementsOnly()
    or some other mechanism to make sure the instance does not provide
    IAcquirer.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignored): ...

class WrapperWidgetTraversal(FormWidgetTraversal):
    """Allow traversal to widgets via the ++widget++ namespace. The context
    is the from layout wrapper.

    The caveat about security above still applies!
    """
