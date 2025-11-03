from Products.CMFCore import interfaces

__all__ = ["IMembershipTool"]

class IMembershipTool(interfaces.IMembershipTool):
    def getMemberInfo(memberId=None) -> None:
        """Return 'harmless' Memberinfo of any member, such as full name,
        location, etc
        """
