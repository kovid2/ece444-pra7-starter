def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def is_missing(value):
    return value is None


def broken_total():
    return missing_total
