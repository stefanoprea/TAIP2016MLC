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

def randword(f,length):
    pos=randint(0,length-1)
    f.seek(pos)
    t=f.read(1)
    while t!="" and not t.isspace():
        t=f.read(1)
    t=f.readline().strip().strip(punctuation)
    if t!="" and isNoun(t): #numai substantive
        return t
    else:
        return randword(f,length)

def main():
    if len(sys.argv)<4:
        print("Usage: python "+sys.argv[0]+" infile.txt outfile.txt nrofpairs")
        return
    #does not check duplicate pairs
    with open(sys.argv[1],"r")as f,open(sys.argv[2],"w+") as g:
        f.seek(0,2)
        length=f.tell()
        nrofpairs=int(sys.argv[3])
        i = nrofpairs
        while i!=0:
            a,b=randword(f,length),randword(f,length)
            if a!=b:
                i-=1
                g.write(a+" "+b+"\n")
                print(str(i)+" pairs to do")
        f.close()
        g.close()

if __name__ == "__main__":
    main()
            
