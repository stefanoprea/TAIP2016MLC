Noile perechi de cuvinte pot fi adaugate la baza de date cu preferred=True, astfel:<br>
 - download prefer.sh, prefer.py si NewDefoeRobinsonCrusoe.txt
 - sh prefer.sh NewDefoeRobinsonCrusoe.txt
 
----------------

Pentru makemigrations si migrate:
    In directorul mysite (cel care contine directorul polls)
    sh setup.sh

Porneste serverul cu:
    python manage.py runserver

In browserul web: 
    127.0.0.1:8000/polls/
    
Poti crea cu cont admin cu: python manage.py createsuperuser <br>
Si apoi accesezi cu: 127.0.0.1:8000/admin/

Pentru a crea perechi de cuvinte: python makePairs.py infile.in outfile.txt 1000 utf-16<br>
Default encoding pentru infile este utf-8

Pentru a adauga perechi de cuvinte:
- sh addWordpairsToDatabase.sh adauga perechile din toate fisierele cu extensia .txt din directorul mysite
- fisierele trebuie sa contina perechi de cuvinte separate prin whitespace, cate o pereche pe un rand (vezi cuvinte.txt pentru exemplu)

To do:
- css
