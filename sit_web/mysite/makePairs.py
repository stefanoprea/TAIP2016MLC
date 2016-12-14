#!/usr/bin/python
from random import randint
import sys,os
from string import punctuation

try:
    from nltk.corpus import wordnet
    def isNoun(t):
        return len(wordnet.synsets(t,pos=wordnet.NOUN))!=0
except:
    def isNoun(t):
        return os.system("wordnet "+t+" -synsn >/dev/null")!=0

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
        if t!="" and isNoun(t) and len(t)>4: #numai substantive
            return t
    return randword(f,length,enc)

def main():
    if len(sys.argv)<4:
        print("Usage: python "+sys.argv[0]+" infile.txt outfile.txt nrofpairs [encoding]\nDefault encoding of infile is utf-8.")
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
        i = nrofpairs
        while i!=0:
            a,b=randword(f,length,enc),randword(f,length,enc)
            if a!=b:
                i-=1
                g.write(a+" "+b+"\n")
                print(str(i)+" pairs to do")
        f.close()
        g.close()

if __name__ == "__main__":
    main()
            
