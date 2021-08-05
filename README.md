The first thing to do is to clone the repository:

$ https://github.com/mahitmangal/sms.git
$ cd project folder

Create a virtual environment to install dependencies in and activate it:

$ virtualenv venv -p python3
$ source env/bin/activate

Then install the dependencies:

(venv)$ pip install -r requirements.txt

Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/

For super user login use 
admin /admin@123

Admin panel helps to view registerd model values 

