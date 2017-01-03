"""Flask-IPInfo
-------------

This library get some useful information from flask's request object.Such as 
IP Address, ISP, Location, Web Browser, Operating System, etc.
"""

import os
import sys
import flask_ipinfo
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system("del /Q dist\\*")
    os.system("python setup.py bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
long_description = ''
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

#Get version
version = flask_ipinfo.__version__

setup(
    name='Flask-IPInfo',
    version=version,
    url='http://github.com/borisliu/flask-ipinfo/',
    license='MIT',
    author='borisliu',
    author_email='boris_cn@263.net',
    description='Get IP, ISP, Location, OS from flask request',
    long_description=long_description,
    platforms=['all'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='flask ip address browser',
    py_modules=['flask_ipinfo'],
    install_requires=['Flask'],
)