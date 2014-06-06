from app import db

class MenuItem( db.Document ):
	title = db.StringField( required = True, max_length = 255 )
	url = db.StringField( required = True, max_length = 255 )
	parent = db.ReferenceField( "self", required = False )
	position = db.IntField( default = 0 )

	@property
	def children( self ):
		"""
		Returns nested to self menu items.
		"""
		return self.objects( parent = self.id )
