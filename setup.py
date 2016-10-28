#!/usr/bin/env python3
import os
import sys
from setuptools import setup

__version__ = "0.1.0"

if sys.argv[-1] == 'publish':
    # if os.system("pip3 freeze | grep wheel"):
    #     print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
    #     sys.exit()
    os.system("python3 setup.py sdist upload")
    os.system("python3 setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("    git tag -a {0} -m 'version {0}'".format(__version__))
    print("    git push --tags")
    sys.exit()

setup(
    name="estrato",
    version=__version__,
    author="Ale",
    author_email="hi@ale.rocks",
    description="Interact with an Electrum / Stratum server.",
    url="https://github.com/iamale/estrato",
    py_modules=["estrato"],
    install_requires=[
        "prompt-toolkit==1.0.8",
        "connectrum==0.5.0",
    ],
    entry_points="""
        [console_scripts]
        estrato=estrato:main
    """,
)
