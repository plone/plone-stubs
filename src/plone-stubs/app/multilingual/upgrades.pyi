SHARED_NAME: str
OLD_PREFIX: str
PROFILE_ID: str

def reimport_css_registry(context) -> None: ...
def migration_pam_1_to_2(context) -> None:
    """Migration plone.app.multilingual 1.x to 2.0 by renaming existing
    language folders and creating new LRF containers where existing
    objects are moved into. Old shared content is moved to portal
    root."""

def upgrade_to_3(context) -> None: ...
def upgrade_to_4(context) -> None: ...
def update_old_layouts(context) -> None:
    """We may have no longer existing layouts layouts set."""

def fix_indonesian_language(context) -> None:
    """Fix the Indonesian language root folder, if it is there.

    Indonesian needs special handling: its language code "id" is not allowed in
    Plone as content id, so its LRF is called "id-id".
    Not all parts of the code were always aware of this.
    Result is that this LRF may have English (or nothing) as language.
    """
