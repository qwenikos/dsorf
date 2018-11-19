
sudo apt-get install python3-pip
---------------------------------------

##install virtualenv

##python 2.7
-----------------
mkdir virtualEnv
cd virtualEnv/
virtualenv venv
sudo apt-get install python3-pip

##to activate
source venv/bin/activate

##to deactivate
deactivate

##python3
--------------
virtualenv -p python3 venv3

After that you have to install all other package with venv3 activated


---------------------------------------
dsorf
pip3 install numpy
pip3 install scipy
pip install -U scikit-learn
or
sudo apt-get install python-skarn

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

## in model blank=True means required=False for derived form




------------------------------------------------
install database backed sessions
add 'django.contrib.sessions' to your INSTALLED_APPS
run manage.py migrate 