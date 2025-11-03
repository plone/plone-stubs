from zope.interface import Interface

class IMailHost(Interface):
    def send(
        messageText,
        mto=None,
        mfrom=None,
        subject=None,
        encode=None,
        charset=None,
        msg_type=None,
    ) -> None:
        """Send mail."""
