from z3c.relationfield import relation

class StagingRelationValue(relation.RelationValue):
    @classmethod
    def get_relations_of(cls, obj, from_attribute=None):
        """a list of relations to or from the passed object"""
