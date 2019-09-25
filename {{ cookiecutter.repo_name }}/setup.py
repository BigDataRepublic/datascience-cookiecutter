from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.0.0",
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}/*']),
    install_requires=install_requires,
)
