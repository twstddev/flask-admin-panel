from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.menuitems.forms import MenuItemForm

module = Blueprint( "menuitems:admin", __name__, url_prefix = "/admin/menuitems" )

@module.route( "/" )
def index():
	"""
	Displays a list of menu items in admin panel.
	"""
	return render_template( "menuitems/index.html" )

@module.route( "/new", methods = [ "GET", "POST" ] )
def new():
	"""
	Displays creation form or creates a menu item if FORM is valid.
	"""
	form = MenuItemForm( request.form )

	if form.validate_on_submit():
		flash( "A menu item has been created", "success" )
		return redirect( url_for( "menuitems:admin.index" ) )

	return render_template( "menuitems/new.html", form = form )
	
