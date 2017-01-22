from nltk.corpus import wordnet as wn


def synonyms(word1, word2):
    word1_synonyms = list()
    for syn in wn.synsets(word1):
        for l in syn.lemmas():
            word1_synonyms.append(l.name().replace("_", " "))

    word2_synonyms = list()
    for syn in wn.synsets(word2):
        for l in syn.lemmas():
            word2_synonyms.append(l.name().replace("_", " "))

    if word1 in word2_synonyms or word2 in word1_synonyms:
        return 4

    return 0


def wup_similarity(word1, word2):
    s1 = wn.synsets(word1)[0]
    s2 = wn.synsets(word2)[0]
    return 4 * s1.wup_similarity(s2)


if __name__ == '__main__':
    print synonyms('courage', 'bravery')
    print wup_similarity('lion', 'tiger')
