# This application is structured as follows:
Firstly, we have Three files 
wsgi.py which is the configuration file for the gunicorn server,
The requirements.txt file which has all the dependencies and libraries the user will install to run the app,
app.py which is the application itself.

# Procedure to run the app
create a folder then move inside 
use the command python3 -m venv venv to create a virtual environment
use the command source venv/bin/activate to activate the virtual environment
type the command pip install -r requirements.txt to install all libraries and dependencies

# Procedure to run the app
type the command gunicorn wsgi:app to run the app on the gunicorn server
access the running app on your browser at 127.0.0.1:8000
