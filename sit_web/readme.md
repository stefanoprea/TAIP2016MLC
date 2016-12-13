Pentru makemigrations si migrate:
    In directorul mysite (cel care contine directorul polls)
    sh setup.sh

Porneste serverul cu:
    python manage.py runserver

In browserul web: 
    127.0.0.1:8000/polls/
    
Poti crea cu cont admin cu: python manage.py createsuperuser <br>
Si apoi accesezi cu: 127.0.0.1:8000/admin/

Pentru a adauga perechi de cuvinte:
- sh adaugaWordpairs.sh adauga perechile din toate fisierele cu extensia .txt din directorul mysite
- fisierele trebuie sa contina perechi de cuvinte separate prin whitespace, cate o pereche pe un rand (vezi cuvinte.txt pentru exemplu)

To do:
- css
- adauga perechi de cuvinte
