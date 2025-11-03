from _typeshed import Incomplete

class rest:
    """Converts from reST to HTML.

      >>> transform = rest()
      >>> class D:
      ...     def setData(self, data):
      ...         self.value = data

      >>> data = transform.convert(\'*hello world*\', D())
      >>> print(data.value)
      <p><em>hello world</em></p>
      <BLANKLINE>

    We want the \'raw\' and \'include\' directives to be disabled by
    default:

      >>> try:
      ...     out = transform.convert(\'.. raw:: html\\n  :file: <isonum.txt>\', D())  # noqa
      ... except NotImplementedError:
      ...     print(\'Good\')
      ... else:
      ...     if "&quot;raw&quot; directive disabled." in out.value:
      ...         print(\'Good\')
      ...     else:
      ...         print(\'Failure\')
      Good

      >>> try:
      ...     out = transform.convert(\'.. include:: <isonum.txt>\', D())
      ... except NotImplementedError:
      ...     print(\'Good\')
      ... else:
      ...     if "&quot;include&quot; directive disabled." in out.value:
      ...         print(\'Good\')
      ...     else:
      ...         print(\'Failure\')
      Good
    """

    inputs: Incomplete
    output: str
    config: Incomplete
    config_metadata: Incomplete
    def __init__(self, name=None, **kwargs) -> None: ...
    def name(self): ...
    def convert(self, orig, data, **kwargs): ...

def register(): ...
