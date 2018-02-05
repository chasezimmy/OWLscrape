from setuptools import setup

setup(
    name='owlscrape',
    entry_points={
        'console_scripts': [
            'owlscrape = main:main',
        ],
    }
)