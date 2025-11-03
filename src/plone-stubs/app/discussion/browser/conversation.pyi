def traverse_parents(context): ...

class ConversationView:
    def enabled(self):
        """Returns True if discussion is enabled for this conversation.

        This method checks five different settings in order to figure out if
        discussion is enable on a specific content object:

        1) Check if discussion is enabled globally in the plone.app.discussion
           registry/control panel.

        2) Check if the allow_discussion boolean flag on the content object is
           set. If it is set to True or False, return the value. If it set to
           None, try further.

        3) Check if discussion is allowed for the content type.
        """
