# setup.py

from setuptools import setup, find_packages

# from .Boba.cli import * # may not need :-(

setup(
    name='boba',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'script_name=Boba.cli:cli',
        ],
    },
)
