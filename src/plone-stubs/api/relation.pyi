from plone.dexterity.content import DexterityContent
from z3c.relationfield import RelationValue

ITERATE_RELATION_NAME: str | None
StagingRelationValue: type[RelationValue] | None

def get(
    source: DexterityContent | None = None,
    target: DexterityContent | None = None,
    relationship: str | None = None,
    unrestricted: bool = False,
    as_dict: bool = False,
) -> list[RelationValue] | dict[str, list[RelationValue]]:
    """Get specific relations given a source/target/relationship.

    :param source: Object that the relations originate from.
    :param target: Object that the relations point to.
    :param relationship: Relationship name.
    :param unrestricted: If true bypass permission-check on source and target.
    :param as_dict: If true, return a dictionary with the relationship name as keys.
    :returns: A list of relations or dict if as_dict=True
    :raises: InvalidParameterError
    """

def create(
    source: DexterityContent,
    target: DexterityContent,
    relationship: str,
) -> None:
    """Create a relation from source to target using zc.relation.

    :param source: [required] Object that the relation will originate from.
    :param target: [required] Object that the relation will point to.
    :param relationship: [required] Relationship name.
    :raises: InvalidParameterError
    """

def delete(
    source: DexterityContent | None = None,
    target: DexterityContent | None = None,
    relationship: str | None = None,
) -> None:
    """Delete relation or relations.

    :param source: Object that the relation originates from.
    :param target: Object that the relation points to.
    :param relationship: Relationship name.
    :raises: InvalidParameterError
    """
