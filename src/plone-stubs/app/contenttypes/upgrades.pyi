from _typeshed import Incomplete

logger: Incomplete

def update_type_icons(context) -> None:
    """Update portal_type icons.

    We want to update two things:

    - the icon_expr property of the portal_type
    - the icon_expr property of the view and edit actions.

    This is for the standard types defined here, plus the Plone Site.

    An earlier version of this upgrade step did this in xml in an upgrade
    profile.  This led to duplicate view and edit actions, because the xml did
    not contain a category for the action.
    A second try with xml still resulted in duplicate view actions,
    and the view and edit actions were invisible.

    Conclusion: if we want to do this in xml, we must specify *all* properties.
    And we do not want this, because these properties may have been changed
    by the user.
    So: we do it in Python.
    """
