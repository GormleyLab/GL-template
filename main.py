import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from package_name import Class_name, function_name, __version__

def main():
    print(f"Package version: {__version__}")
    object_name = Class_name("Hello, world!")
    object_name.method_name()
    function_name()

if __name__ == "__main__":
    main()