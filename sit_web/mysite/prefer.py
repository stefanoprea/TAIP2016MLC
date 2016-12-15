#!/bin/sh

import os
from polls.models import *

def mergePair(a,b):
    if a<b:
        return a+"\t"+b
    else:
        return b+"\t"+a

def prefer(infile):
    for l in open(infile):
            l=l.split()
            if len(l)>=2:
                t=mergePair(l[0],l[1])
                f=Wordpair.objects.filter(text=t)
                if len(f)==0:            
                    w=Wordpair(text=t)
		else:
                    w=f[0]
                w.preferred=True
                w.save()