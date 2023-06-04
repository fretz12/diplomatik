import re

MERGE_WHITESPACES_PATTERN = re.compile(r"\s+")

def merge_whitespaces(target: str) -> str:
    """
    Removes all leading and trailing whitespaces from a string. Merges multiple whitespaces into a single one

    :param target: the string to clean up
    :return: the cleaned up string
    """
    return MERGE_WHITESPACES_PATTERN.sub(" ", target).strip()
