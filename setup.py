"""
Flask-IPInfo
-------------

This library get some useful information from flask's request object.Such as 
IP Address, ISP, Location, Web Browser, Operating System, etc.
"""
from setuptools import setup


setup(
    name='Flask-IPInfo',
    version='1.0',
    url='http://github.com/borisliu/flask-ipinfo/',
    license='MIT',
    author='boris liu',
    author_email='boris_cn@263.net',
    description='Get IP, ISP, Location, OS from flask request',
    long_description=__doc__,
    py_modules=['flask_ipinfo'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)