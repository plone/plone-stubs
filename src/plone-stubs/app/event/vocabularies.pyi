def SynchronizationStrategies(context):
    """Vocabulary for icalendar synchronization strategies.

    SYNC_KEEP_NEWER:  Import, if the imported event is modified after the
                      existing one.
    SYNC_KEEP_MINE:   On conflicts, just do nothing.
    SYNC_KEEP_THEIRS: On conflicts, update the existing event with the external
                      one.
    SYNC_NONE:        Don't synchronize but import events and create new ones,
                      even if they already exist. For each one, create a new
                      sync_uid.
    """
