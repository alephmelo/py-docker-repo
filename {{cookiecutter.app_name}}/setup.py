""" Base setup script """

from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.app_name}}",
    version="1.0",
    description="{{cookiecutter.app_desc}}",
    url="{{cookiecutter.website}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    packages=find_packages(),
    # Entry Point
    entry_points={"console_scripts": []},
    # Core Dependencies
    install_requires=[],
    # Dev/Test Dependencies
    extras_require={"dev": [], "test": []},
    # Scripts
    scripts=[],
)
