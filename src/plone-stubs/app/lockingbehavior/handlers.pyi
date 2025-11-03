def protect_edit_form(obj, event) -> None:
    """If the object is locked for the current user, let's redirect to
    the view of the object, where the lockinfo viewlet usually is.
    """
