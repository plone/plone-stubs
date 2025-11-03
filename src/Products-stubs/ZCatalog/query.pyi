from _typeshed import Incomplete

class IndexQueryParseError(Exception): ...

class IndexQuery:
    """
    This class provides functionality to hide the internals of a query
    send from the Catalog/ZCatalog to an index._apply_index() method.

    The class understands the following type of parameters:

    - old-style parameters where the query for an index as value inside
      the request dictionary where the index name is the name of the key.

    - dictionary-style parameters specify a query for an index as
      an entry in the request dictionary where the key corresponds to the
      name of the index and the key is a dictionary with the parameters
      passed to the index.

      Allowed keys of the parameter dictionary:

      'query'  - contains the query (either string, list or tuple) (required)

      other parameters depend on the the index.
    """

    operators: Incomplete
    id: Incomplete
    options: Incomplete
    keys: Incomplete
    def __init__(
        self,
        request,
        iid,
        options=(),
        operators=("or", "and"),
        default_operator: str = "or",
    ) -> None:
        """Parse a query from the ZPublisher and return a uniform
        datastructure back to the _apply_index() method of the index.

          query -- the query dictionary send from the ZPublisher
          iid     -- Id of index
          options -- a list of options the index is interested in
          operators -- a tuple of allowed operators
          default_operator -- the default operator
        """
    @property
    def operator(self): ...
    @operator.setter
    def operator(self, value) -> None: ...
    def get(self, key, default_v=None): ...
    def set(self, key, value) -> None: ...
