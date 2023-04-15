import sys, inspect

def is_mod_function(mod, func):
    return inspect.isfunction(func) and inspect.getmodule(func) == mod

def list_functions(mod):
    return [func.__name__ for func in mod.__dict__.itervalues() 
            if is_mod_function(mod, func)]


print ('functions in current module:\n', list_functions(sys.modules[manager]))