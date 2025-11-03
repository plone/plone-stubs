def opt(start, end, size, orphan, sequence_length):
    """Calculate start, end, batchsize"""

def calculate_pagenumber(elementnumber, batchsize, overlap: int = 0):
    """Calculate the pagenumber for the navigation"""

def calculate_pagerange(pagenumber, numpages, pagerange):
    """Calculate the pagerange for the navigation quicklinks"""

def calculate_quantum_leap_gap(numpages, pagerange):
    """Find the QuantumLeap gap. Current width of list is 6 clicks (30/5)"""

def calculate_leapback(pagenumber, numpages, pagerange):
    """Check the distance between start and 0 and add links as necessary"""

def calculate_leapforward(pagenumber, numpages, pagerange):
    """Check the distance between end and length and add links as necessary"""
