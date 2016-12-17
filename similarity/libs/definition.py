#/usr/bin/env python

from nltk.corpus import wordnet as wn


# Returns 3 in one word appears in other word definition
# Return 3.5 if both words appear in other definition
# Return None if there is no match
def similarity(word1, word2):
    def find_in_definition(word1, word2):
        for x in wn.synsets(word1):
            name = x.name().split(".")[0]
            print(x.name() , " ",x.definition())
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
    

if __name__ == "__main__":
    print(similarity("water", "ice"))

