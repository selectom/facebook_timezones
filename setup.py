# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

version = '0.2'

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='facebook_timezones',
    packages=['facebook_timezones'],
    version=version,
    description='Helpers for using timezones in the Facebook Graph API.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    author='Alon Diamant',
    author_email='alon@mayple.com',
    url='https://github.com/mayple/facebook_timezones',
    download_url='https://github.com/mayple/facebook_timezones/archive/{}.tar.gz'.format(version),
    keywords=['facebook', 'graph api', 'timezone', 'timezones', 'facebook timezones', 'marketing api'],
    license='MIT',
    tests_require=['pytz'],
    classifiers=[  # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
    ],
)
