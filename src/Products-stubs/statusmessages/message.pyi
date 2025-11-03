from _typeshed import Incomplete

class Message:
    """A single status message.

    Let's make sure that this implementation actually fulfills the
    'IMessage' API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IMessage, Message)
      True

      >>> status = Message(u'this is a test', type=u'info')
      >>> status.message == 'this is a test'
      True

      >>> status.type == 'info'
      True

    It is quite common to use MessageID's as status messages:

      >>> from zope.i18nmessageid import MessageFactory
      >>> from zope.i18nmessageid import Message as I18NMessage
      >>> msg_factory = MessageFactory('test')

      >>> msg = msg_factory(u'test_message', default=u'Default text')

      >>> status = Message(msg, type=u'warn')
      >>> status.type == 'warn'
      True

      >>> type(status.message) is I18NMessage
      True

      >>> status.message.default == 'Default text'
      True

      >>> status.message.domain == u'test'
      True

    """

    message: Incomplete
    type: Incomplete
    def __init__(self, message, type: str = "") -> None: ...
    def __eq__(self, other): ...
    def encode(self):
        """
        Encode to a cookie friendly format.

        The format consists of a two bytes length header of 11 bits for the
        message length and 5 bits for the type length followed by two values.
        """

def decode(value):
    """
    Decode messages from a cookie

    We return the decoded message object, and the remainder of the cookie
    value as bytes (it can contain further messages).

    We expect at least 2 bytes (size information).
    """
