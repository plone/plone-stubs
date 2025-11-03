from zope.interface import Interface

class IReferenceFactories(Interface):
    """Contains Factories knowing how and where to instantiate an object.

    Caution:

    - This interface is in flux and probably will change when implementing
      Archteypes reference support.
    - The source parameter will disappear as soon as on save the back
      references are save with the object.
    """
    def invokeFactory(repo_clone, source, selector=None) -> None:
        """Invokes the right factory for the object in a history.

        Returns the attached object and it's id.
        """
    def hasBeenMoved(obj, source) -> None:
        """Returns True if the object has been moved away from ``source``."""
