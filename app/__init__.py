from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from app.utils import ObjectIDConverter, helpers as utils
from app.middlewares import methodrewrite
from .template_helpers import helpers

app = Flask( __name__ )
#app.wsgi_app = methodrewrite.MethodRewriteMiddleware( app.wsgi_app )
app.config.from_object( "config" )
app.debug = app.config[ "DEBUG" ]

db = MongoEngine( app )

@app.errorhandler( 404 )
def not_found( error ):
	"""
	Loads given template on 404 error.
	"""
	return render_template( "404.html" ), 404

if not app.config[ "DEBUG" ]:
	utils.generate_secret_key( app )

from app.menuitems.models import MenuItem

@app.route( "/" )
def test_menu_item():
	menu_item = MenuItem( title = "Home", url = "/" )
	menu_item.save()

	return menu_item.title

# register templates helpers
@app.context_processor
def inject_helpers():
	return helpers

# automatically convert mongodb objectids to string values
app.url_map.converters[ 'ObjectId' ] = ObjectIDConverter

from app.menuitems.views import module as user_module
app.register_blueprint( user_module )
