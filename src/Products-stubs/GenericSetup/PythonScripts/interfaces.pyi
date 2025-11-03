from zope.interface import Interface

class IPythonScript(Interface):
    """Web-callable scripts written in a safe subset of Python.

    The function may include standard python code, so long as it does not
    attempt to use the "exec" statement or certain restricted builtins.
    """
    def read() -> None:
        """Generate a text representation of the Script source.

        Includes specially formatted comment lines for parameters, bindings
        and the title.
        """
    def write(text) -> None:
        """Change the Script by parsing a read()-style source text."""
