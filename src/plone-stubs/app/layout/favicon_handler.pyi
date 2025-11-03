from plone.registry.interfaces import IRecordModifiedEvent
from plone.registry.recordsproxy import RecordsProxy as RecordsProxy

def updateMimetype(settings: RecordsProxy, event: IRecordModifiedEvent = None): ...
