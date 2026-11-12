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


# Final fix, I fixed the real defect instead of disabling the rule.
def broken_total():
    missing_total = 0
    return missing_total
