def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


# Added violation: E711 - if value == None:
# None is a singleton, so use is None. == can be fooled by a custom __eq__
def is_missing(x):
    return x is None
