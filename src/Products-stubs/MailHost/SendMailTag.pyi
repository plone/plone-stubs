from _typeshed import Incomplete

class SendMailTag:
    """the send mail tag, used like thus:

    <dtml-sendmail mailhost="someMailHostID">
    to: person@their.machine.com
    from: me@mymachine.net
    subject: just called to say...

    boy howdy!
    </dtml-sendmail>

    Text between the sendmail and /sendmail tags is processed
    by the MailHost machinery and delivered.  There must be at least
    one blank line seperating the headers (to/from/etc..) from the body
    of the message.

    Instead of specifying a MailHost, an smtphost may be specified
    ala \'smtphost="mail.mycompany.com" port=25\' (port defaults to 25
    automatically).  Other parameters are

    * mailto -- person (or comma-seperated list of persons) to send the
    mail to.  If not specified, there **must** be a to: header in the
    message.

    * mailfrom -- person sending the mail (basically who the recipient can
    reply to).  If not specified, there **must** be a from: header in the
    message.

    * subject -- optional subject.  If not specified, there **must** be a
    subject: header in the message.

    * encode -- optional encoding. Possible values are: \'base64\' and
     \'quoted-printable\'.

    """

    name: str
    blockContinuations: Incomplete
    encode: Incomplete
    encoding: Incomplete
    smtphost: Incomplete
    mailhost: Incomplete
    section: Incomplete
    args: Incomplete
    mailto: Incomplete
    mailfrom: Incomplete
    subject: Incomplete
    port: Incomplete
    def __init__(self, blocks, encoding=None) -> None: ...
    def render(self, md): ...
    __call__ = render
