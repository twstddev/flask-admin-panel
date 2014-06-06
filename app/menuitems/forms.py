from flask.ext.mongoengine.wtf import model_form
from app.menuitems.models import MenuItem

MenuItemForm = model_form( MenuItem )
