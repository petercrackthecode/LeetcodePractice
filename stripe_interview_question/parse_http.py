"""

Part 1

In an HTTP request, the Accept-Language header describes the list of
languages that the requester would like content to be returned in. The header
takes the form of a comma-separated list of language tags. For example:

Accept-Language: en-US, fr-CA, fr-FR

means that the reader would accept:

1. English as spoken in the United States (most preferred)
2. French as spoken in Canada
3. French as spoken in France (least preferred)

We're writing a server that needs to return content in an acceptable language
for the requester, and we want to make use of this header. Our server doesn't
support every possible language that might be requested (yet!), but there is a
set of languages that we do support. Write a function that receives two arguments:
an Accept-Language header value as a string and a set of supported languages,
and returns the list of language tags that will work for the request. The
language tags should be returned in descending order of preference (the
same order as they appeared in the header).

In addition to writing this function, you should use tests to demonstrate that it's
correct, either via an existing testing system or one you create.

Examples:

parse_accept_language(
"en-US, fr-CA, fr-FR", # the client's Accept-Language header, a string
["fr-FR", "en-US"] # the server's supported languages, a set of strings
)
returns: ["en-US", "fr-FR"]

parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
returns: ["fr-FR"]

parse_accept_language("en-US", ["en-US", "fr-CA"])
returns: ["en-US"]

- return a list of string
- sort the list descending order of preference

question to ask: is each language in supported_langs unique?

- have the ans list to save the result: ans:List[str] = []
- convert the supported language into a set called supported_langs_lookup = set(supported_langs)
- loop thru each language in headers:
    - if language exists in supported_langs_lookup:
        - append language to ans
- sort the ans array descendingly according to each language's index in supported_langs_lookup
- return ans
"""

from operator import index
from typing import List, Set


def parse_accept_language(headers: str, supported_langs: List[str]) -> List[str]:
    ans: List[str] = []

    desired_langs = [s.strip() for s in headers.split(",") if s.strip() != ""]

    supported_langs_lookup: Set[str] = set(supported_langs)
    index_lookup = dict(zip(supported_langs, range(len(supported_langs))))

    print(f"index_lookup = {index_lookup}")

    for lang in desired_langs:
        if lang in supported_langs_lookup:
            ans.append(lang)

    ans.sort(key=lambda _lang: index_lookup[_lang], reverse=True)

    return ans


# ans = parse_accept_language(
#     "en-US, fr-CA, fr-FR",  # the client's Accept-Language header, a string
#     ["fr-FR", "en-US"],  # the server's supported languages, a set of strings
# )  # returns: ["en-US", "fr-FR"]


# ans = parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])  # returns: ["fr-FR"]

ans = parse_accept_language("en-US", ["en-US", "fr-CA"])  # returns: ["en-US"]

print(f"ans = {ans}")
