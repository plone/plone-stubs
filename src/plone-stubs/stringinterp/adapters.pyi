from _typeshed import Incomplete
from Acquisition import Implicit

class ContextWrapper(Implicit):
    """Wrapper for context"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, **kwargs): ...

class BaseSubstitution:
    """Base substitution"""

    wrapper: Incomplete
    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

class UrlSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ParentIdSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class IdSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ParentUrlSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class TitleSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ParentTitleSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class DescriptionSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class TypeSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class CreatorSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class CreatorFullNameSubstitution(CreatorSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class CreatorEmailSubstitution(CreatorSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class CreatorsSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class CreatorsEmailsSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ContributorsSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ContributorsEmailsSubstitution(BaseSubstitution):
    category: str
    description: Incomplete
    def safe_call(self): ...

class SubjectSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class FormatSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class LanguageSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class IdentifierSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class RightsSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ReviewStateSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ReviewStateTitleSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class DateSubstitution(BaseSubstitution):
    def formatDate(self, adate): ...

class CreatedSubstitution(DateSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class EffectiveSubstitution(DateSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ExpiresSubstitution(DateSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ModifiedSubstitution(DateSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class MemberSubstitution(BaseSubstitution):
    mtool: Incomplete
    gtool: Incomplete
    def __init__(self, context) -> None: ...
    def getMembersFromIds(self, ids): ...
    def getPropsForMembers(self, members, propname): ...
    def getPropsForIds(self, ids, propname): ...

class MailAddressSubstitution(MemberSubstitution):
    def getEmailsForRole(self, role): ...

class OwnerEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ReviewerEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ReaderEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ContributorEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class EditorEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ManagerEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class MemberEmailSubstitution(MailAddressSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class UserEmailSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class UserFullNameSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class UserIdSubstitution(BaseSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class ChangeSubstitution(BaseSubstitution):
    def lastChangeMetadata(self, id): ...

class LastChangeCommentSubstitution(ChangeSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class LastChangeTitleSubstitution(ChangeSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class LastChangeTypeSubstitution(ChangeSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class LastChangeActorIdSubstitution(ChangeSubstitution):
    category: Incomplete
    description: Incomplete
    def safe_call(self): ...

class PortalSubstitution(BaseSubstitution):
    category: Incomplete
    portal: Incomplete
    def __init__(self, context) -> None: ...

class PortalURLSubstitution(PortalSubstitution):
    description: Incomplete
    def safe_call(self): ...

class PortalTitleSubstitution(PortalSubstitution):
    description: Incomplete
    def safe_call(self): ...
