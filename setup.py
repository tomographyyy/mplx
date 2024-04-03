from setuptools import setup, find_packages

def load_requires_from_file(filepath):
    with open(filepath) as fp:
        return [pkg_name.strip() for pkg_name in fp.readlines()]

setup(
    name='mplx',  # name of package shown by "pip list"
    version="0.0.3",
    description="matplotlib extension package",
    author='Tomohiro TAKAGAWA',
    packages=find_packages(),  # define list of modules
    license='Apache-2.0',
    install_requires=load_requires_from_file("requirements.txt")
)
