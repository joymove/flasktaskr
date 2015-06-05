import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))
d = os.path.dirname(__name__)
print d
print os.path.abspath(d)
DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
