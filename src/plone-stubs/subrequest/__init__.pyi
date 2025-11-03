from plone.subrequest.subresponse import SubResponse as SubResponse

__all__ = ["SubResponse", "subrequest"]

def subrequest(url, root=None, stdout=None, exception_handler=None): ...
