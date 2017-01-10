import os
from polls.models import *

def mergePair(a,b):
    if a<b:
        return a+"\t"+b
    else:
        return b+"\t"+a

for f in os.listdir(os.getcwd()+"/perechi"):
    if f[-4:]==".txt":
        for l in open("./perechi/"+f):
            l=l.split()
            if len(l)>=2:
                t=mergePair(l[0],l[1])
                if len(Wordpair.objects.filter(text=t))==0:            
                    Wordpair(text=t).save()
