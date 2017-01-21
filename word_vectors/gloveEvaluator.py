
"""Modified from the gloVe script evaluate.py.
http://nlp.stanford.edu/software/GloVe-1.2.zip
"""

import numpy as np

def loadVectors(vectors_file,vocab_file=None):
    """Constructor calls it. vectors_file is the path to the vector file. Will load the vectors into RAM!!!"""
    if vocab_file==None:vocab_file=vectors_file
    
    with open(vocab_file, 'r') as f:
        words = [x.rstrip().split(' ')[0] for x in f.readlines()]
    with open(vectors_file, 'r') as f:
        vectors = {}
        for line in f:
            vals = line.rstrip().split(' ')
            vectors[vals[0]] = map(float, vals[1:])

    vocab_size = len(words)
    vocab = {w: idx for idx, w in enumerate(words)}
    ivocab = {idx: w for idx, w in enumerate(words)}

    vector_dim = len(vectors[ivocab[0]])
    W = np.zeros((vocab_size, vector_dim))
    for word, v in vectors.iteritems():
        if word == '<unk>':
            continue
        W[vocab[word], :] = v

    # normalize each word vector to unit variance
    W_norm = np.zeros(W.shape)
    d = (np.sum(W ** 2, 1) ** (0.5))
    W_norm = (W.T / d).T
    return (W_norm,vocab,ivocab)
    
class wordVectors():
    """
    from gloveEvaluator import wordVectors
    x=wordVectors("glove.6B.50d.txt") #load word vector file into RAM
    #x=wordVectors("vector.txt",cased=True) pentru vectori cased
    x.evalWordpair("winter","summer")
    x.evalWordpair("snow","icecream")
    x.evalWordpair("copou","sleigh") #None
    del x #free RAM
    """
    def __init__(self,filename,cased=False):
        self.W,self.vocab,self.ivocab=loadVectors(filename)
        self.cased=cased
    def evalWordpair(self,foo,bar,tolower=None):
        """Evaluate cosine distance between foo and bar."""
        W,vocab=self.W,self.vocab
        if tolower==None:
            tolower= not self.cased
        if tolower:
            foo,bar=foo.lower(),bar.lower()
        if foo not in vocab or bar not in vocab:
            return None
        else:
            return abs(4*np.dot(W[vocab[foo]],W[vocab[bar]]))

