def get_change_note(request, default=None):
    """Returns the changeNote submitted with this request. The changeNote
    is read from the form-field (see behaviors.IVersionable)
    """
