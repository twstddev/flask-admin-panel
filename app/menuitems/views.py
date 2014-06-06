from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.views import MethodView, View
from app.menuitems.models import MenuItem
from app.menuitems.forms import MenuItemForm

module = Blueprint( "menuitems:admin", __name__, url_prefix = "/admin/menuitems" )

class NewMenuItemView( MethodView ):
	"""
	Represents page where a new menu item can be added.
	"""
	def get( self ):
		"""
		Displays creation form
		"""
		form = MenuItemForm( request.form )
		return render_template( "menuitems/new.html", form = form )


class MenuItemsAdminView( MethodView ):
	"""
	Represents default controller API interface.
	"""
	def get( self, menu_item_id ):
		"""
		Displays a list of menu items in admin panel
		or creates a new one on POST request.
		"""
		if menu_item_id is None:
			menu_items = MenuItem.objects.all()
			print menu_items
			return render_template( "menuitems/index.html", menu_items = menu_items )
		else:
			return redirect( url_for( "menuitems:admin.menu_items",  ) )

	def post( self, menu_item_id ):
		"""
		Creates a new menu item.
		"""
		if menu_item_id is None:
			form = MenuItemForm( request.form )

			if form.validate_on_submit():
				new_menu_item = MenuItem()
				form.populate_obj( new_menu_item )
				new_menu_item.save()

				flash( "A menu item has been created", "success" )
				return redirect( url_for( "menuitems:admin.menu_items", menu_item_id = None ) )
			else:
				return render_template( "menuitems/new.html", form = form )



# Register resource routes
menu_item_new_view = NewMenuItemView.as_view( "new_menu_item" )
menu_items_admin_view = MenuItemsAdminView.as_view( "menu_items" )

module.add_url_rule( "/", defaults = { "menu_item_id" : None },
	view_func = menu_items_admin_view, methods = [ "GET", "POST" ] )

module.add_url_rule( "/new/", view_func = menu_item_new_view, methods = [ "GET" ] )

	
