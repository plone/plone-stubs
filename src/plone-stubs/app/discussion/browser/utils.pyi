def format_author_name_with_suffix(comment, request, anonymous_user_suffix=...):
    """Format author name with suffix for anonymous users.

    Returns the author name with a suffix (Guest) appended for anonymous
    comments. The suffix is translated to the current user\'s language.

    Args:
        comment: The comment object
        anonymous_user_suffix: The suffix message to append (e.g., _("(Guest)"))
        request: The request object for translation context

    Returns:
        str: The formatted author name
    """
