from distutils.core import setup

from sarch import __version__


setup(
    name='Sarch',
    version=__version__,
    packages=['sarch',],
    entry_points = {
        'console_scripts': ['sarch=sarch.interface.sarch:main'],
    },
)