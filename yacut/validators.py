import re
from settings import SHORT_ID_REGEX


def isalnum_check(short_id):
    pattern = re.compile(SHORT_ID_REGEX)
    result = re.search(pattern, short_id)
    return result is not None
