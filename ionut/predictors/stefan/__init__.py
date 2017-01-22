import os

import numpy as np


def load_vectors(vectors_file, vocab_file=None):
    """Constructor calls it. vectors_file is the path to the vector file. Will load the vectors into RAM!!!"""
    if vocab_file is None:
        vocab_file = vectors_file

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
    return W_norm,vocab,ivocab


class WordVectors:
    """
    from gloveEvaluator import wordVectors
    x=wordVectors("glove.6B.50d.txt") #load word vector file into RAM
    #x=wordVectors("vector.txt",cased=True) pentru vectori cased
    x.evalWordpair("winter","summer")
    x.evalWordpair("snow","icecream")
    x.evalWordpair("copou","sleigh") #None
    del x #free RAM
    """
    def __init__(self,filename):
        print 'loading vectors'
        self.W, self.vocab, self.ivocab = load_vectors(filename)
        print 'done'

    def eval_wordpair(self, word1, word2, to_lower=False):
        """Evaluate cosine distance between foo and bar."""
        W, vocab = self.W, self.vocab
        if to_lower:
            word1, word2 = word1.lower(), word2.lower()
        if word1 not in vocab or word2 not in vocab:
            return None
        else:
            return abs(4 * np.dot(W[vocab[word1]], W[vocab[word2]]))

w2v = WordVectors(os.environ['LEX_VECTOR'])


def word2vec(word1, word2):
    return w2v.eval_wordpair(word1, word2)


if __name__ == '__main__':
    print word2vec('song', 'poem')
