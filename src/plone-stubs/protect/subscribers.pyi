from _typeshed import Incomplete

LOGGER: Incomplete

def onUserLogsIn(event) -> None:
    """
    since we already write to the database when a user logs in,
    let's check for key rotation here
    """
