class ATDProxyView:
    """Proxy for the 'After the Deadline' spellchecker"""
    def checkDocument(self):
        """Proxy for the AtD service's checkDocument function
        See http://www.afterthedeadline.com/api.slp for more info.
        """
