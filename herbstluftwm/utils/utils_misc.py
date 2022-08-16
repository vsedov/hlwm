def item_in(iter: iter, item: object) -> bool:
    """
    Check if an item is in an iterable.
    """
    return any(map(lambda x: x == item, iter))


def contains(iter_or_string, item) -> bool:
    """
    Check if an item is in an iterable or string.
    """

    return item in iter_or_string


def has_duplicates(iter: iter) -> bool:
    """
    Check if an iterable has duplicates.
    """

    return len(iter) != len(set(iter))


def super_unique(iter: iter) -> list:
    """
    Return a list of unique items in an iterable.
    """

    return list(set(iter))
