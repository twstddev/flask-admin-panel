import os
import sys

def generate_secret_key( app, filename = "secret" ):
	"""
	Generates a new secret key that will be used
	across the application for securing sensitive data.
	"""
	filename = os.path.join( app.config[ "BASE_PATH" ], filename )
	print filename
	sys.exit( 1 )

