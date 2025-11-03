from _typeshed import Incomplete
from configparser import ConfigParser

logger: Incomplete

class CMFConfigParser(ConfigParser):
    """This our wrapper around ConfigParser to
    solve a few minor niggles with the code"""

    OPTCRE: Incomplete
    def optionxform(self, optionstr):
        """
        Stop converting the key to lower case, very annoying for security etc
        """

class FSMetadata:
    def __init__(self, filename) -> None: ...
    def read(self) -> None:
        """Find the files to read, either the old security and
        properties type or the new metadata type"""
    def getProxyRoles(self):
        """Returns the proxy roles"""
    def getSecurity(self):
        """Gets the security settings"""
    def getProperties(self):
        """Gets the properties settings"""
