from _typeshed import Incomplete

security: Incomplete
ManageUsers: Incomplete
ManageGroups: str

@security.private
def setDefaultRoles(permission, roles) -> None:
    """Set the defaults roles for a permission."""

SearchPrincipals: str
SetOwnPassword: str
