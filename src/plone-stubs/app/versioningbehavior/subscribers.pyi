def create_version_on_save(context, event) -> None:
    """Creates a new version on a versionable object when the object is saved.
    A new version is created if the type is automatic versionable and has
    changed or if the user has entered a change note.
    """

def create_initial_version_after_adding(context, event) -> None:
    """Creates a initial version on a object which is added to a container
    and may be just created.
    The initial version is created if the content type is versionable,
    automatic versioning is enabled for this type and there is no initial
    version. If a changeNote was entered it's used as comment.
    """
