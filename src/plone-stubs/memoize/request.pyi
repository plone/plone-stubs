from _typeshed import Incomplete

__all__ = ["cache", "memoize_diy_request", "store_in_annotation_of"]

class RequestMemo:
    key: str
    arg: Incomplete
    def __init__(self, arg: int = 0) -> None: ...
    def __call__(self, func): ...

def store_in_annotation_of(expr): ...
def cache(get_key, get_request: str = "request"): ...

memoize_diy_request = RequestMemo
