import os

BASE_PATH = os.path.abspath( os.path.dirname( __file__ ) )

DEBUG = True

SECRET_KEY = "testsecret"
CSRF_SESSION_KEY = "yoursecretkey"
WTF_CSRF_SECRET_KEY = "yoursecretkey"

# Database connection details go here.
MONGODB_SETTINGS = {
	"DB" : "app",
}
