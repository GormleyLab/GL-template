# This is the main file for the package
# It is used to import the class and function from the other files
# It also contains the version of the package

from .__about__ import __version__
from .class_example import Class_name
from .utils_example import function_name

__all__ = ['Class_name', 'function_name', '__version__']