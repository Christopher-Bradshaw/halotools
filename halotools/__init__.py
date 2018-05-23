"""
Halotools is a specialized python package
for building and testing models of the galaxy-halo connection,
and analyzing catalogs of dark matter halos.
"""
from ._astropy_init import *

from . import custom_exceptions

# If we aren't running setup.py, ensure that we are running a compiled version
if not _ASTROPY_SETUP_:
    try:
        import halotools._compiler
    except ImportError:
        raise ImportError("""You should not try import halotools from its source directory;
        please leave the halotools source tree and relaunch your python interpreter from there""")

def test_installation(*args, **kwargs):
    kwargs.setdefault('args', '')
    if kwargs['args']:
        kwargs['args'] += ' '
    kwargs['args'] += '-m installation_test'
    return test(*args, **kwargs)
