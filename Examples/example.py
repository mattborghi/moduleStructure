# Add to the path the package directory before importing
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Import project files Method 1
from TestProject.Decoder import Main

a = Main.MyClass()
