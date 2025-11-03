from plone.restapi.services import Service

MAX: int

def make_summary(obj, request):
    """Add UID to metadata_fields."""

def get_relations(
    sources=None,
    targets=None,
    relationship=None,
    request=None,
    unrestricted: bool = False,
    onlyBroken: bool = False,
    max=None,
):
    """Get valid relations."""

def relation_stats(): ...
def getBrokenRelationNames(): ...
def getStaticCatalogVocabularyQuery(vocabularyFactoryName): ...

class GetRelations(Service):
    """Get relations or stats

        source: UID of content item
        target: UID of content item
        relation: name of a relation
        max: integer: maximum of results
        onlyBroken: boolean: dictionary with broken relations per relation type
        query_source: Restrict relations by path or SearchableText
        query_target: Restrict relations by path or SearchableText

    Returns:
        stats if no parameter, else relations
    """
    def __init__(self, context, request) -> None: ...
    def reply(self): ...
