from setuptools import setup, find_packages

setup(
    name='advent_of_code',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
    author='Samuel Gómez',
    author_email='samuel.gomez.balderas@gmail.com',
    description='A project for Advent of Code',
    url='https://github.com/Sierra-034/advent-of-code-2024',
)