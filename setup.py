#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path


setup(
    name="mplcyberpunk",
    version="0.1.0",
    url="https://github.com/dhaitz/mplcyberpunk",
    license='MIT',

    author="Dominik Haitz",
    author_email="dominik.haitz@gmx.de",

    description="Add-on for Matplotlib",

    long_description=Path('README.md').open().read(),


    packages=["mplcyberpunk"],
    package_data={
      'mplcyberpunk': ['data/*.mplstyle'],
   },

    # Derive version from git. If HEAD is at the tag, the version will be the tag itself.
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "0.0.1"
    },
    setup_requires=Path('requirements.txt').open().read(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)
