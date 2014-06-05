from flask import Flask, render_template
from .utils import generate_secret_key

app = Flask( __name__ )
app.config.from_object( "config" )
app.debug = app.config[ "DEBUG" ]

@app.errorhandler( 404 )
def not_found( error ):
	"""
	Loads given template on 404 error.
	"""
	return render_template( "404.html" ), 404

if not app.config[ "DEBUG" ]:
	generate_secret_key( app )

