import os

BASE_PATH = os.path.abspath( os.path.dirname( __file__ ) )

DEBUG = True

SECRET_KEY = ""
CSRF_SESSION_KEY = "yoursecretkey"

# Database connection details go here.
MONGODB_SETTINGS = {
	"DB" : "app",
}
