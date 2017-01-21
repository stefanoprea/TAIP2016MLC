from nltk.corpus import wordnet


syns = wordnet.synsets ("dog")

print (syns)

syns = wordnet.synsets ("car")

print (syns)

syns = wordnet.synsets ("machinery")

print (syns)


w1 = wordnet.synset ("car.n.01")
w2 = wordnet.synset ("machinery.n.01")

print (w1.wup_similarity(w2)*4)

w1 = wordnet.synset ("dog.n.01")
w2 = wordnet.synset ("car.n.01")

print (w1.wup_similarity(w2)*4)

w1 = wordnet.synset ("dog.n.01")
w2 = wordnet.synset ("machinery.n.01")

print (w1.wup_similarity(w2)*4)

w1 = wordnet.synset ("car.n.01")
w2 = wordnet.synset ("car.n.01")

print (w1.wup_similarity(w2)*4)


synonyms = []

for syn in wordnet.synsets ("car"):
    for l in syn.lemmas ():
        synonyms.append (l.name().replace("_", " "))

print (set(synonyms))
word = input("word = ?\n")

print(word)
if word in synonyms:
    print("4")
else:
    print("0")


