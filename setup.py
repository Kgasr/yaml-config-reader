# setup.py

from setuptools import setup, find_packages

setup(
    name='yaml_config_reader',
    version='0.0.1',
    description='It reads the yaml config entire file or specific section',
    url='https://github.com/Kgasr/yaml-config-reader',
    author='Karan Gupta',
    author_email='karangupta125@gmail.com',
    packages=find_packages(),
    install_requires=['PyYAML'],
)
