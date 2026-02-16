from plone.dexterity.content import DexterityContent
from typing import Literal
from typing import overload
from z3c.relationfield import RelationValue

ITERATE_RELATION_NAME: str | None
StagingRelationValue: type[RelationValue] | None

@overload
def get(
    source: DexterityContent | None = None,
    target: DexterityContent | None = None,
    relationship: str | None = None,
    unrestricted: bool = False,
    as_dict: Literal[False] = False,
) -> list[RelationValue]:
    """Get specific relations given a source/target/relationship.

    :param source: Object that the relations originate from.
    :type source: Content object
    :param target: Object that the relations point to.
    :type target: Content object
    :param relationship: Relationship name.
    :type relationship: string
    :param unrestricted: If true bypass permission-check on source and target.
    :type unrestricted: boolean
    :param as_dict: If true, return a dictionary with the relationship name as keys.
    :type as_dict: boolean
    :returns: A list of relations.
    :rtype: list of RelationValue objects
    """

@overload
def get(
    source: DexterityContent | None = None,
    target: DexterityContent | None = None,
    relationship: str | None = None,
    unrestricted: bool = False,
    *,
    as_dict: Literal[True],
) -> dict[str, list[RelationValue]]:
    """Get specific relations as a dictionary.

    :param source: Object that the relations originate from.
    :type source: Content object
    :param target: Object that the relations point to.
    :type target: Content object
    :param relationship: Relationship name.
    :type relationship: string
    :param unrestricted: If true bypass permission-check on source and target.
    :type unrestricted: boolean
    :param as_dict: If true, return a dictionary with the relationship name as keys.
    :type as_dict: boolean
    :returns: A dict with relationship name as keys.
    :rtype: dict of string to list of RelationValue objects
    """

def create(
    source: DexterityContent,
    target: DexterityContent,
    relationship: str,
) -> None:
    """Create a relation from source to target using zc.relation.

    :param source: [required] Object that the relation will originate from.
    :type source: Content object
    :param target: [required] Object that the relation will point to.
    :type target: Content object
    :param relationship: [required] Relationship name.
    :type relationship: string
    """

def delete(
    source: DexterityContent | None = None,
    target: DexterityContent | None = None,
    relationship: str | None = None,
) -> None:
    """Delete relation or relations.

    :param source: Object that the relation originates from.
    :type source: Content object
    :param target: Object that the relation points to.
    :type target: Content object
    :param relationship: Relationship name.
    :type relationship: string
    """
