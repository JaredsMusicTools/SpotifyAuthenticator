from setuptools import find_packages, setup
import os
import sys

PKG_NAME = "SpotifyAuthenticator"

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, PKG_NAME, 'version.py')) as f:
    exec(f.read(), version)

setup(
    name = PKG_NAME,
    version=version['__version__'],
    description=('Flask application for authenticating Spotify users'),
    long_description=long_description,
    author='Jared Dyreson',
    author_email='jareddyreson@csu.fullerton.edu',
    url='https://github.com/JaredDyreson/SpotifyAuthenticator',
    license='GNU GPL-3.0',
    packages=[PKG_NAME],
    install_requires = [
      'Flask-OAuthlib==0.9.5',
      'Flask==1.0.2'
    ],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages()
    classifiers=['Programming Language :: Python :: 3.8']
)
