from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name="rabobank_training",
    version="0.0.0",
    packages=find_packages(include=['rabobank_training',]),
    install_requires=install_requires,
)
