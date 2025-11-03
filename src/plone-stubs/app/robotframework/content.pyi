from plone.app.robotframework.remote import RemoteLibrary

HAS_DEXTERITY_RELATIONS: bool

class Content(RemoteLibrary):
    def delete_content(self, uid_or_path) -> None:
        """Delete content by uid or path"""
    def create_content(self, *args, **kwargs):
        """Create content and return its UID"""
    def set_field_value(self, uid, field, value, field_type) -> None:
        """Set field value with a specific type"""
    def uid_to_url(self, uid):
        """Return absolute path for an UID"""
    def path_to_uid(self, path):
        """Return UID for an absolute path"""
    def fire_transition(self, content, action) -> None:
        """Fire workflow action for content"""
    do_action_for = fire_transition
    def global_allow(self, type_, value: bool = True) -> None:
        """Allow type to be added globally."""

def prefill_image_types(kwargs) -> None: ...
def random_image(): ...
