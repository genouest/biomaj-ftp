try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from distutils.command.install import install
import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()


config = {
    'description': 'BioMAJ FTP server',
    'long_description': README + '\n\n' + CHANGES,
    'author': 'Olivier Sallou',
    'url': 'http://biomaj.genouest.org',
    'download_url': 'http://biomaj.genouest.org',
    'author_email': 'olivier.sallou@irisa.fr',
    'version': '3.0.7',
     'classifiers': [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    'install_requires': ['requests',
                         'pymongo>=3.12.3,<4',
                         'python-consul',
                         'pyftpdlib',
                         'biomaj_core',
                         'biomaj_user',
                         'PyYAML',
                         'python-consul'
                         ],
    'tests_require': ['nose', 'mock'],
    'packages': find_packages(),
    'include_package_data': True,
    'scripts': ['bin/biomaj_ftp_service.py'],
    'name': 'biomaj_ftp'
}

setup(**config)
