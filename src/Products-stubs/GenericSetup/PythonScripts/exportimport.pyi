from ..utils import BodyAdapterBase
from _typeshed import Incomplete

class PythonScriptBodyAdapter(BodyAdapterBase):
    """Body im- and exporter for PythonScript."""

    body: Incomplete
    mime_type: str
    suffix: str
