import re


def fix_quote(text):
    pattern = r">.*?<"
    match = re.search(pattern, str(text))
    if match:
        quote = match.group()
        return quote


def fix_author(text):
    pattern = r">.*?<"
    match = re.search(pattern, str(text))
    if match:
        author = match.group()
        return author
