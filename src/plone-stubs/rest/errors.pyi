from Products.Five.browser import BrowserView

HAS_WSGI: bool

class ErrorHandling(BrowserView):
    """This view is responsible for serializing unhandled exceptions, as well
    as handling 404 Not Found errors and redirects.
    """
    def __call__(self) -> None: ...
    def render_exception(self, exception): ...
    def render_traceback(self, exception): ...
    def find_redirect_if_view_or_service(self, old_path_elements, storage):
        """Find redirect for URLs like:
        - http://example.com/object/namedservice/param
        - http://example.com/object/@@view/param
        - http://example.com/object/template

        This combines the functionality of the find_redirect_if_view() and
        find_redirect_if_template() methods of the original FourOhFourView into
        one, and also makes it support named services.

        For this to also work for named services we use a different strategy
        here: Based on old_path_elements, try to find the longest stored
        redirect (if any), and consider the remaining path parts the remainder
        (view, template, named services plus possible params) that will need
        to be appended to the new object path.
        """
    def attempt_redirect(self):
        """Check if a redirect is needed, and perform it if necessary.

        Returns True if a redirect has been performed, False otherwise.

        This method is based on FourOhFourView.attempt_redirect() from
        p.a.redirector. It's copied here because we want to answer redirects
        to non-GET methods with status 307, but since this method locks the
        response status, we wouldn't be able to change it afterwards.
        """
