# dsorf
install django 
sudo apt-get install python3-django

sudo pip3 install Django==2.1.3

django-admin --version
install crispy-forms
pip3 install --user django-crispy-forms

After create a new model in django you have to
Activating models

python3 manage.py makemigrations predictor
python3 manage.py sqlmigrate predictor 0001
python3 manage.py migrate

#install sqlite browser
sudo add-apt-repository ppa:linuxgndu/sqlitebrowser-testing
sudo apt-get update && sudo apt-get install sqlitebrowser

#if you like to remove it
sudo apt-get remove sqlitebrowser