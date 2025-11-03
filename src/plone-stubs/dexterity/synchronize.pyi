def synchronized(lock):
    """Decorate a method with this and pass in a threading.Lock object to
    ensure that a method is synchronised over the given lock.
    """
