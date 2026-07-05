import sys
import os

# Put the repository root on sys.path so `import python.<subpackage>` resolves.
# conftest.py lives at python/tests/, so the repo root is three levels up.
_repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)
