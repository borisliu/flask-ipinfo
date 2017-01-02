"""
Flask-IPInfo
-------------

This library get some useful information from flask's request object.Such as 
IP Address, ISP, Location, Web Browser, Operating System, etc.
"""
import os
import sys
import flask_ipinfo

if sys.argv[-1] == 'publish':
    os.system("del /Q dist\\*")
    os.system("python setup.py bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

from setuptools import setup

#Get version
version = flask_ipinfo.__version__

#Get long description.
long_description = ""
with open("README.rst") as f:
    long_description = f.read()

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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=['flask_ipinfo'],
    install_requires=[
        'Flask'
    ],
)