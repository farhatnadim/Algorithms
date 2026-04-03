import sys
import os

# Add the repository root and DataStructures to Python path for imports
_repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _repo_root)
sys.path.insert(0, os.path.join(_repo_root, 'DataStructures'))
