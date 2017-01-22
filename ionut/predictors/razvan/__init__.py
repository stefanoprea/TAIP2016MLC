import json
import requests

from nltk.corpus import wordnet as wn


def definition(word1, word2):
    """
    Returns 3 in one word appears in other word definition
    Return 3.5 if both words appear in other definition
    Return None if there is no match
    """
    def find_in_definition(word1, word2):
        for x in wn.synsets(word1):
            name = x.name().split(".")[0]
            if word1 == name and word2 in x.definition():
                return True
        return False
    found_first = find_in_definition(word1, word2)
    found_second = find_in_definition(word2, word1)

    if found_first and found_second:
        return 3.5
    if found_first or found_second:
        return 3
    return None


def lexical_field(word1, word2):
    def get_field(word):
        payload = {"entry": word}
        data = json.loads(requests.post("https://www.twinword.com/graph/api/v4/context/visualize/", data=payload).text)
        if 'context' not in data:
            return
        context = data["context"]
        theme = []
        for rel in data["relation"]:
            for con in context:
                if con in rel:
                    theme.append(rel[con])

        return context, theme

    def find(word, context, theme):
        return word in context, word in theme

    w1_context, w1_theme = get_field(word1)
    w2_context, w2_theme = get_field(word2)

    w1_found_context, w1_found_theme = find(word1, w2_context, w2_theme)
    w2_found_context, w2_found_theme = find(word2, w1_context, w1_theme)

    if w1_found_context and w2_found_context:
        return 4.5
    if w1_found_context or w2_found_context:
        return 4
    if w1_found_theme and w2_found_theme:
        return 3.5
    if w1_found_theme or w2_found_theme:
        return 3
