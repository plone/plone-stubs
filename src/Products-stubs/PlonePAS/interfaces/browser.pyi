from zope.interface import Interface

class IPASInfoView(Interface):
    def hasLoginPasswordExtractor(self) -> None:
        """Check if a login & password extraction plugin is active.

        Check if there is a plugin with an enabled
        ILoginPasswordExtractionPlugin interface. This can be used to
        conditionally show username & password logins.
        """
    def hasOpenIDExtractor(self) -> None:
        """Check if an OpenID extraction plugin is active."""
    def hasOpenIDdExtractor(self) -> None:
        """Check if an OpenID extraction plugin is active.

        BBB Keeping method name with typo for backwards compatibility.
        """

class IPASMemberView(Interface):
    def info(self, userid=None) -> None:
        """Return 'harmless' member info of any user, such as full name,
        location, etc.
        """

class IPASSearchView(Interface):
    def searchUsers(self, sort_by=None, any_field=None, **criteria) -> None:
        """Search for users matching a set of criteria.

        The criteria are a dictionary mapping user properties to values and
        have the semantics declared by IPluggableAuthService.searchUsers().
        Duplicate results returned by PAS are filtered so only the first
        result remains in the result set. The results can be sorted on
        sort_bys (case insensitive).

        In addition, a single search string can be sought in multiple
        fields at a time by passing any_field='your-string'. The fields
        that will be searched are not explicitly enumerated but will be the
        user-facing ones a user would expect to search, such as login name
        and full name. (Perhaps any_field should/could be moved into PAS
        proper. This could be done without breaking code that depends on
        this interface.)

        If you specify both any_field and other criteria that include a
        field that any_field would typically search (such as login name),
        the other criteria will be enforced at the expense of any_field.
        """
    def searchUsersByRequest(self, request, sort_by=None) -> None:
        """Search for users matching a set of criteria found in a request.

        This method will look remove any obvious values from the request
        which are not search criteria. It will also remove any fields
        which have an empty string value.
        Duplicate results returned by PAS are filtered so only the first
        result remains in the result set. The results can be sorted on
        sort_by (case insensitive).
        """
    def searchGroups(self, **criteria) -> None:
        """Search for groups matching a set of criteria.

        The criteria are a dictionary mapping group properties
        to values and have the semantics declared by
        IPluggableAuthService.searchGroups().
        """
    def searchGroupsByRequest(self, request) -> None:
        """Search for groups matching a set of criteria found in a request.

        This method will look remove any obvious values from the request
        which are not search criteria. It will also remove any fields
        which have an empty string value.
        """
    def merge(self, results, key) -> None:
        """merge two search results based on key as the unique criterion"""
    def sort(self, results, key) -> None:
        """sort results on a key"""
