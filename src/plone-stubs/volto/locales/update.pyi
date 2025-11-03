from _typeshed import Incomplete
from pathlib import Path

logger: Incomplete
PATTERN: str
cwd: Incomplete
target_path: Incomplete
locale_path: Incomplete

def get_i18ndude() -> Path: ...

i18ndude: Incomplete
excludes: str

def locale_folder_setup(domain: str): ...
def update_locale() -> None: ...
