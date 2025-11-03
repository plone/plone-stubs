from _typeshed import Incomplete

EXTRACT_BODY: int
EXTRACT_STYLE: int
FIX_IMAGES: int
IMAGE_PREFIX: str
ENABLE_UNO: bool

class word_to_html:
    inputs: Incomplete
    output: str
    output_encoding: str
    tranform_engine: Incomplete
    def name(self): ...
    def convert(self, data, cache, **kwargs): ...

def register(): ...
