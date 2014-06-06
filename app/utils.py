import os
import sys

def generate_secret_key( app, filename = "secret" ):
	"""
	Generates a new secret key that will be used
	across the application for securing sensitive data.
	"""
	filename = os.path.join( app.config[ "BASE_PATH" ], filename )

        try:
            app.config[ "SECRET_KEY" ] = open( filename, "rb" ).read()
        except IOError:
            generated_key =  os.urandom( 24 ).encode( "base-64" )
            
            with open( filename, "w" ) as f:
                f.write( generated_key )
            sys.exit( 1 )


