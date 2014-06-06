from flask import Blueprint, render_template, request, flash

module = Blueprint( "menuitems:admin", __name__, url_prefix = "/admin/menuitems" )

@module.route( "/" )
def index():
	return render_template( "menuitems/index.html" )
