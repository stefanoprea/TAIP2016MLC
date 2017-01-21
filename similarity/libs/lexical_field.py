#!/usr/bin/env python3
import requests
import json

def similarity(word1, word2):
    def get_field(word):
        payload = {"entry": word}
        data = json.loads(requests.post("https://www.twinword.com/graph/api/v4/context/visualize/", data=payload).text)
        context = data["context"]
        theme = []
        for rel in data["relation"]:
            for con in context:
                if con in rel:
                    theme.append(rel[con])

        return context, theme

    def find(word, context, theme):
        return (word in context, word in theme)

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

if __name__ == "__main__":
    print(similarity("rain", "snow"))

