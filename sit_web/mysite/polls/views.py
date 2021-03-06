from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils.encoding import smart_text
from .models import Wordpair,Mysession
from random import randint

def xyzzy(k):
    return "".join(k.split()).lower()

def toList(text):
    l=[]
    for i in text.split(","):
        l.append(int(i))
    return l

def fromList(l):
    l2=[]
    for i in l:
        l2.append(str(i))
    return ",".join(l2)

def mergePair(a,b):
    if a<b:
        return a+"\t"+b
    else:
        return b+"\t"+a

def splitPair(t):
    return tuple(t.split("\t"))

def allIsPeachy(x):
    s=0
    for j in x:
        s+=j
    if s>=10:
        return True
    if s<4:
        return False
    for j in range(len(x)-1):
        if float(x[j]+x[j+1])/s>75.0/100:
            return True
    return False

# Create your views here.

def index(request):

    #if not request.session.get("something"):
    request.session["something"]=True
    key=request.session.session_key

    if key!=None and len(Mysession.objects.filter(sessionkey=key))==0:
        Mysession(sessionkey=request.session.session_key).save()
    x=Mysession.objects.filter(sessionkey=key)
    if len(x)>0:
        s=x[0]
    else:
        s=None
 
    d=request.POST.dict()
    if "wordpair" in d.keys():
        if "logout" in d.keys():
            request.session.flush()
            s=None
            d["dontknow"]=True
        q=Wordpair.objects.get(text=d["wordpair"])
        if "dontknow"not in d.keys():
            l=toList(q.votes)
            l[int(d["option"])]+=1
            if allIsPeachy(l):
                q.finished=True
            q.votes=fromList(l)
            q.nrvotes+=1
            if s!=None:
                s.pairsDone+=1
                s.save()
        if s!=None:
            s.wordpairs.add(q)
            if xyzzy(d["username"]):s.username=xyzzy(d["username"])
            s.save()
            
        q.save()
    q=None
    
    gotQuestion=False
    if s!=None:
        ft=Wordpair.objects.filter(preferred=True,finished=False,nrvotes__gt=0).exclude(mysession__sessionkey=s.sessionkey)
        if len(ft):
            q=ft[randint(0,len(ft)-1)]
            gotQuestion=True
        else:
            ft=Wordpair.objects.filter(preferred=True,nrvotes=0).exclude(mysession__sessionkey=s.sessionkey)
            if len(ft):
                q=ft[randint(0,len(ft)-1)]
                gotQuestion=True
            else:
                ft=Wordpair.objects.filter(finished=False,nrvotes__gt=0).exclude(mysession__sessionkey=s.sessionkey)
                if len(ft):
                    q=ft[randint(0,len(ft)-1)]
                    gotQuestion=True
                else:
                    ft=Wordpair.objects.filter(nrvotes=0).exclude(mysession__sessionkey=s.sessionkey)
                    if len(ft):
                        q=ft[randint(0,len(ft)-1)]
                        gotQuestion=True
    if not gotQuestion:
        ft=Wordpair.objects.all()
        if len(ft):
            q=ft[randint(0,len(ft)-1)]
        else:
            raise Exception("Absolutely no wordpairs in database")

         
    word1,word2=splitPair(q.text)
    return render(request,"polls/index.html",{"word1":word1,"word2":word2,"wordpair":q.text,"username":s.username if s!=None else "", 
    "USERNAME": s.username if s!=None else "UNKNOWN!!!",
    "pairsDone":str(s.pairsDone) if s!=None else "I don't know how many" })

def statistics(request):
    session_list = Mysession.objects.only("username", "pairsDone").filter(username__isnull=False)

    stats = {}
    for item in session_list:
        if item.username not in stats:
            stats[item.username] = 0
        stats[item.username] += item.pairsDone
    html = u"""<!DOCTYPE html>
<html>
<head></head>
<body>
"""
    for item in stats.items():
	username = smart_text(item[0])
	count = item[1]
        html += u"{username}:{count}</br>".format(username=username, count=count)
    html += u"""</body>
</html>
"""
    return HttpResponse(html)

