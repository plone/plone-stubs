from _typeshed import Incomplete
from watchdog.events import FileSystemEventHandler

def TIME(): ...
def WAIT(msg): ...
def ERROR(msg): ...

class Watcher(FileSystemEventHandler):
    allowed_extensions: Incomplete
    forkloop: Incomplete
    observers: Incomplete
    paths: Incomplete
    minimum_wait: Incomplete
    last_event: Incomplete
    def __init__(self, paths, forkloop, minimum_wait: float = 2.0) -> None: ...
    def start(self) -> None:
        """Start file monitoring thread"""
    def on_any_event(self, event) -> None: ...

class ForkLoop:
    fork: bool
    active: bool
    pause: bool
    killed_child: bool
    forking: bool
    exit: bool
    parent_pid: Incomplete
    child_pid: Incomplete
    def __init__(self) -> None: ...
    def isChild(self): ...
    def isChildAlive(self): ...
    def start(self) -> None:
        """Start fork loop"""
    def loop(self) -> None:
        """Magic happens"""
    def forkNewChild(self) -> None:
        """STEP 1 (parent): New child process forking starts by killing the
        current child process.

        """
