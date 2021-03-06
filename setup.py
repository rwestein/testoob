kwargs = {
    'packages' : ['testoob', 'testoob.compatibility', 'testoob.reporting', 'testoob.running', 'testoob.commandline'],
    'package_dir' : {'': 'src'},
    'scripts'  : ['src/testoob/testoob'],

    # meta-data
    'name'             : 'testoob',
    'version'          : '1.16',
    'author'           : 'Ori Peleg',
    'author_email'     : 'testoob@gmail.com',
    'url'              : 'http://code.google.com/p/testoob',
    'download_url'     : 'http://code.google.com/p/testoob/downloads/list',
    'license'          : 'Apache License, Version 2.0',
    'platforms'        : ['any'],
    'description'      : 'Testoob - An advanced unit testing framework',
}

import sys
if sys.platform.startswith("win"):
    kwargs['data_files'] = [('testoob', ['other/setcolor.exe'])],

kwargs['long_description'] = """
Testoob - Python Testing Out Of (The) Box

Testoob is an advanced unit testing framework for Python. It integrates
effortlessly with existing PyUnit (module "unittest") test suites.

Version 1.16 (2009) makes you coffee!
""".strip()

kwargs['classifiers'] = """
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Programming Language :: Python
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
""".strip().splitlines()

# ============================================================================

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

# run setup
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**kwargs)
