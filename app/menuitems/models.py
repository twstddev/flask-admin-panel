from app import db

class MenuItem( db.Document ):
	title = db.StringField( required = True, max_length = 255 )
	url = db.StringField( required = True, max_length = 255 )
	parent = db.ReferenceField( "self", required = False )

	@property
	def children( self ):
		return self.objects( parent = self.id )
