#!/usr/bin/python
from random import randint
import sys,os
from string import punctuation
from nltk.stem import WordNetLemmatizer
lemmatize=WordNetLemmatizer().lemmatize
from nltk.corpus import wordnet
def isNoun(t):
    return len(wordnet.synsets(t,pos=wordnet.NOUN))!=0
def isOther(t):
    return len(wordnet.synsets(t,pos="var"))!=0
def randSyn(t):
    l=wordnet.synsets(t,pos=wordnet.NOUN)
    if len(l)>0:
        return l[randint(0,len(l)-1)].lemmas()[0].name()
    else:
        return ""


def randword(f,length,enc):
    pos=randint(0,length-1)
    f.seek(pos)
    t=f.read(1)
    while len(t)!=0 and ord(t)!=10:
        t=f.read(1)
    l=unicode(f.readline(),enc).split()
    if len(l)>0:
        t=l[randint(0,len(l)-1)]
        t=t.strip().strip(punctuation)
        if t!="" and isNoun(t) and not isOther(t) and len(t)>4: #numai substantive
            return t
    return randword(f,length,enc)

def main():
    if len(sys.argv)<4:
        print("Usage: python "+sys.argv[0]+" infile.txt outfile.txt nrofpairs  [encoding]\nDefault encoding of infile is utf-8.")
        return
    #does not check duplicate pairs
    if len(sys.argv)>=5:
        enc=sys.argv[4]
    else:
        enc="utf-8"
    with open(sys.argv[1],"r")as f,open(sys.argv[2],"w+") as g:
        f.seek(0,2)
        length=f.tell()
        nrofpairs=int(sys.argv[3])
        j=0
        i = nrofpairs//2
        while i!=0:
            a,b=randword(f,length,enc),randword(f,length,enc)
            if a!=b:
                i-=1
                j+=1
                g.write(a+" "+b+"\n")
                print(str(nrofpairs-j)+" pairs to do")
        i = nrofpairs-j
        while i!=0:
            a=randword(f,length,enc)
            b=randSyn(a)
            if b!="" and "_" not in b and lemmatize(a.lower())!=lemmatize(b.lower()):
                i-=1
                j+=1
                g.write(a+" "+b+"\n")
                print(str(nrofpairs-j)+" pairs to do")
        f.close()
        g.close()

if __name__ == "__main__":
    main()
            
