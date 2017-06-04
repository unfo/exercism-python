import collections


def _flatten(_in, depth):
    for item in _in:
        is_iterable = isinstance(item, collections.Iterable)
        is_string = isinstance(item, str)
        if is_iterable and not is_string:
            for _item in _flatten(item, depth+1):
                yield _item
        else:
            if item is not None:
                yield item

def flatten(items):
    return [item for item in _flatten(items, 1)]
