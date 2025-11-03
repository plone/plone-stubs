from _typeshed import Incomplete

FEED_SETTINGS_KEY: str

class FeedSettings:
    context: Incomplete
    annotations: Incomplete
    needs_saving: bool
    site_settings: Incomplete
    def __init__(self, context) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __getattr__(self, name): ...
