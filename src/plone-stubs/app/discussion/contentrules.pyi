from _typeshed import Incomplete
from plone.stringinterp.adapters import BaseSubstitution

class BaseSubstitution:
    """Fallback class if plone.stringinterp is not available"""

    context: Incomplete
    def __init__(self, context, **kwargs) -> None: ...

def execute_comment(event) -> None:
    """Execute comment content rules"""

class CommentSubstitution(BaseSubstitution):
    """Comment string substitution"""
    def __init__(self, context, **kwargs) -> None: ...
    @property
    def event(self):
        """event that triggered the content rule"""
    @property
    def comment(self):
        """Get changed inline comment"""

class Id(CommentSubstitution):
    """Comment id string substitution"""

    category: Incomplete
    description: Incomplete
    def safe_call(self):
        """Safe call"""

class Text(CommentSubstitution):
    """Comment text"""

    category: Incomplete
    description: Incomplete
    def safe_call(self):
        """Safe call"""

class AuthorUserName(CommentSubstitution):
    """Comment author user name string substitution"""

    category: Incomplete
    description: Incomplete
    def safe_call(self):
        """Safe call"""

class AuthorFullName(CommentSubstitution):
    """Comment author full name string substitution"""

    category: Incomplete
    description: Incomplete
    def safe_call(self):
        """Safe call"""

class AuthorEmail(CommentSubstitution):
    """Comment author email string substitution"""

    category: Incomplete
    description: Incomplete
    def safe_call(self):
        """Safe call"""
