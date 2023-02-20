#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Hampton Hoover",
    author_email='whh2t@mtmail.mtsu.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is my analysis on the mental wellbeing of medical students",
    entry_points={
        'console_scripts': [
            'data4950_project=data4950_project.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='data4950_project',
    name='data4950_project',
    packages=find_packages(include=['data4950_project', 'data4950_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/whh96/data4950_project',
    version='0.0.1',
    zip_safe=False,
)
