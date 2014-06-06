def is_current_module( module_name ):
	"""
	Checks if the current module name is set and
	compares it against the given name.
	"""
	return "active" if module_name == current_module else ""


helpers = {
	"is_current_module" : is_current_module
}


